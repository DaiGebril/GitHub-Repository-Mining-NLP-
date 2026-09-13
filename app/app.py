# ============================================================
# GITHUB REPOSITORY MINING - FINAL GUI
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from pathlib import Path
import plotly.express as px

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
from sklearn.metrics.pairwise import cosine_similarity

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="GitHub Repository Mining",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    # PageRank
    pr_df = pd.read_csv(RESULTS_DIR / "pagerank_results.csv")

    # Rules
    rules = pd.read_csv(RESULTS_DIR / "rules (1).csv")

    # Original sample
    df_sample = pd.read_csv(DATA_DIR / "sample_data.csv")

    # HITS
    hub_df = pd.read_csv(RESULTS_DIR / "hubs.csv")
    authorities_df = pd.read_csv(RESULTS_DIR / "authorities.csv")

    # BERT
    classification_df = pd.read_csv(RESULTS_DIR / "classification_results.csv")
    bert_df = pd.read_csv(RESULTS_DIR / "bert_data.csv")
    embeddings = np.load(MODELS_DIR / "embeddings.npy")

    return (
        pr_df,
        rules,
        df_sample,
        hub_df,
        authorities_df,
        classification_df,
        bert_df,
        embeddings
    )

# Load all
(
    pr_df,
    rules,
    df_sample,
    hub_df,
    authorities_df,
    classification_df,
    bert_df,
    embeddings
) = load_data()

# ============================================================
# LOAD GRAPH
# ============================================================

try:
    with open(MODELS_DIR / "graph.pkl", "rb") as f:
        G = pickle.load(f)
except:
    G = None

# ============================================================
# SIMILARITY FUNCTION
# ============================================================

def find_similar_repos(repo_name, bert_df, embeddings, top_n=5):

    idx = bert_df[bert_df['Name'] == repo_name].index[0]

    similarities = cosine_similarity(
        [embeddings[idx]],
        embeddings
    )[0]

    similar_indices = similarities.argsort()[::-1][1:top_n+1]

    results = []

    for i in similar_indices:
        results.append({
            "Name": bert_df.iloc[i]['Name'],
            "Similarity": similarities[i],
            "Stars": bert_df.iloc[i]['Stars']
        })

    return results

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📊 GitHub Mining Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "PageRank",
        "Association Rules",
        "BERT",
        "HITS"
    ]
)

# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.title("🏠 GitHub Repository Mining Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Repositories", len(df_sample))

    with col2:
        st.metric("Association Rules", len(rules))

    with col3:
        st.metric(
            "Top PageRank",
            round(pr_df['PageRank_Score'].max(), 4)
        )

    with col4:
        st.metric(
            "Average Stars",
            int(df_sample['Stars'].mean())
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # Top Repositories
    with col1:

        st.subheader("⭐ Top 10 Repositories")

        st.dataframe(
            pr_df[
                ['Name', 'PageRank_Score', 'Stars']
            ].head(10),
            use_container_width=True
        )

    # Category Distribution
    with col2:

        st.subheader("🤖 Repository Categories")

        cat_counts = classification_df['Category'].value_counts()

        fig = px.pie(
            values=cat_counts.values,
            names=cat_counts.index,
            title="BERT Classification"
        )

        st.plotly_chart(fig, use_container_width=True)

# ============================================================
# PAGERANK PAGE
# ============================================================

elif page == "PageRank":

    st.title("⭐ PageRank Analysis")

    st.subheader("Top 20 Influential Repositories")

    st.dataframe(
        pr_df[
            ['Name', 'PageRank_Score', 'Stars']
        ].head(20),
        use_container_width=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # Top PageRank
    with col1:

        fig, ax = plt.subplots(figsize=(8, 6))

        top10 = pr_df.head(10)

        ax.barh(
            top10['Name'],
            top10['PageRank_Score']
        )

        ax.invert_yaxis()

        ax.set_xlabel("PageRank Score")
        ax.set_title("Top 10 by PageRank")

        st.pyplot(fig)

    # Stars
    with col2:

        fig, ax = plt.subplots(figsize=(8, 6))

        top_stars = pr_df.nlargest(10, 'Stars')

        ax.barh(
            top_stars['Name'],
            top_stars['Stars']
        )

        ax.invert_yaxis()

        ax.set_xlabel("Stars")
        ax.set_title("Top 10 by Stars")

        st.pyplot(fig)

    st.markdown("---")

    st.subheader("📈 Stars vs PageRank")

    fig, ax = plt.subplots(figsize=(10, 6))

    scatter = ax.scatter(
        pr_df['Stars'],
        pr_df['PageRank_Score'],
        alpha=0.6
    )

    ax.set_xlabel("Stars")
    ax.set_ylabel("PageRank Score")

    st.pyplot(fig)

# ============================================================
# ASSOCIATION RULES PAGE
# ============================================================

elif page == "Association Rules":

    st.title("🔗 Association Rules (FP-Growth)")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Rules", len(rules))

    with col2:
        st.metric("Repositories", len(df_sample))

    st.markdown("---")

    st.subheader("🏆 Top Rules by Lift")

    st.dataframe(
        rules[
            ['antecedents', 'consequents', 'lift', 'confidence']
        ].head(10),
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🔍 Search Rules")

    tech = st.text_input(
        "Search technology (Python, React, Docker...)"
    )

    if tech:

        filtered = rules[
            rules['antecedents'].astype(str).str.contains(
                tech,
                case=False
            ) |
            rules['consequents'].astype(str).str.contains(
                tech,
                case=False
            )
        ]

        st.dataframe(
            filtered.head(20),
            use_container_width=True
        )

    st.markdown("---")

    st.subheader("📈 Confidence vs Lift")

    fig, ax = plt.subplots(figsize=(10, 6))

    scatter = ax.scatter(
        rules['confidence'],
        rules['lift'],
        alpha=0.6
    )

    ax.set_xlabel("Confidence")
    ax.set_ylabel("Lift")

    st.pyplot(fig)

# ============================================================
# BERT PAGE
# ============================================================

elif page == "BERT":

    st.title("🤖 BERT Analysis")

    col1, col2 = st.columns(2)

    # Category Distribution
    with col1:

        st.subheader("📊 Category Distribution")

        cat_counts = classification_df['Category'].value_counts()

        fig = px.pie(
            values=cat_counts.values,
            names=cat_counts.index
        )

        st.plotly_chart(fig, use_container_width=True)

    # Confidence
    with col2:

        st.subheader("📈 Confidence Distribution")

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.hist(
            classification_df['Confidence'],
            bins=20
        )

        ax.set_xlabel("Confidence")

        st.pyplot(fig)

    st.markdown("---")

    st.subheader("🔍 Similar Repository Search")

    repo_search = st.selectbox(
        "Choose Repository",
        bert_df['Name'].tolist()
    )

    if repo_search:

        similar = find_similar_repos(
            repo_search,
            bert_df,
            embeddings
        )

        st.write(f"Repositories similar to: **{repo_search}**")

        for i, repo in enumerate(similar, 1):

            st.write(
                f"{i}. {repo['Name']} "
                f"(Similarity: {repo['Similarity']:.4f}) "
                f"| ⭐ {repo['Stars']}"
            )

    st.markdown("---")

    st.subheader("📋 Classification Results")

    st.dataframe(
        classification_df.head(20),
        use_container_width=True
    )

# ============================================================
# HITS PAGE
# ============================================================

elif page == "HITS":

    st.title("📈 HITS Analysis")

    col1, col2 = st.columns(2)

    # Hubs
    with col1:

        st.subheader("Top Hubs")

        st.dataframe(
            hub_df.head(10),
            use_container_width=True
        )

    # Authorities
    with col2:

        st.subheader("Top Authorities")

        st.dataframe(
            authorities_df.head(10),
            use_container_width=True
        )

    st.markdown("---")

    st.subheader("📊 Hub vs Authority")

    merged = hub_df.merge(
        authorities_df,
        on='URL'
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    scatter = ax.scatter(
        merged['Hub_Score'],
        merged['Authority_Score'],
        alpha=0.6
    )

    ax.set_xlabel("Hub Score")
    ax.set_ylabel("Authority Score")

    st.pyplot(fig)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "📊 GitHub Repository Mining Project | "
    "PageRank | HITS | FP-Growth | BERT 🚀"
)