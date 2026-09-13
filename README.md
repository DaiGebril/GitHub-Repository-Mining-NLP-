# 🔎 GitHub Repository Mining

## 📌 Project Overview

GitHub Repository Mining is a data mining and NLP project designed to analyze GitHub repositories and discover meaningful patterns, relationships, rankings, and semantic similarities between repositories.

The project combines:

- 📊 Data Mining
- 🌐 Graph Mining
- 📈 PageRank
- 🔗 HITS Algorithm
- 🛒 Association Rule Mining
- 🤖 BERT-based NLP
- 🔍 Semantic Similarity
- 📊 Interactive Streamlit Dashboard

The project analyzes a dataset of GitHub repositories and provides an interactive dashboard for exploring the discovered insights.

---

## 🎯 Project Objectives

The main objectives of the project are to:

- Analyze GitHub repository metadata.
- Identify highly influential repositories using graph-based ranking.
- Discover relationships between repositories through shared topics.
- Find frequently occurring patterns using association rule mining.
- Classify repositories using NLP techniques.
- Measure semantic similarity between repositories.
- Visualize the extracted insights through an interactive dashboard.

---

## 📊 Dataset

The project uses a GitHub repository dataset containing repository-level information such as:

- Repository name
- Stars
- Topics
- Repository metadata
- Other repository-related features

To make the analysis computationally manageable while preserving both popular and diverse repositories, a hybrid sampling strategy was used.

### Hybrid Sampling

The final sample contains:

**3,000 repositories**

The sample combines:

- 1,500 repositories with the highest number of stars.
- 1,500 randomly selected repositories.

This approach provides a balance between highly popular repositories and a broader representation of GitHub projects.

---

## 🧹 Data Preprocessing

The preprocessing stage includes:

- Data cleaning
- Handling missing values
- Feature preparation
- Topic processing
- Data transformation
- Feature engineering
- Hybrid sampling

The processed dataset is then used by the different mining and NLP components.

---

## 🌐 Graph Mining

A graph representation of the repositories was constructed based on shared topics.

### Graph Concept

- **Nodes** → GitHub repositories
- **Connections** → Relationships between repositories based on shared topics

This graph structure allows the project to apply graph-ranking algorithms and identify important repositories.

---

## 📈 PageRank

PageRank is used to measure the relative importance of repositories within the constructed graph.

Repositories with stronger connections to other important repositories receive higher PageRank scores.

### Example Results

| Repository | PageRank Score | Stars |
|---|---:|---:|
| NativeScript | 0.0039 | 22,976 |
| 30-Days-Of-JavaScript | 0.0029 | 38,463 |
| novu | 0.0027 | 24,441 |
| storybook | 0.0026 | 80,398 |
| pulumi | 0.0025 | 17,581 |

The highest PageRank score in the dashboard is approximately:

**0.0039**

---

## 🔗 HITS Algorithm

The project also applies the **HITS (Hyperlink-Induced Topic Search)** algorithm.

HITS identifies two types of important nodes:

### ⭐ Hubs

Repositories that point toward or are strongly connected with authoritative repositories.

### 👑 Authorities

Repositories that are considered important based on their relationships within the graph.

The resulting hub and authority scores are stored separately and visualized through the dashboard.

---

## 🛒 Association Rule Mining

Association Rule Mining is used to discover relationships between repository topics.

The project uses frequent itemset mining and association rules to identify combinations of topics that frequently occur together.

### Example

A discovered rule can represent a relationship such as:

```text
Topic A → Topic B

with measurements such as:

Support
Confidence
Lift
```

The dashboard provides an interactive view of the discovered association rules.

The current dashboard contains:

**72 association rules**

---

## 🤖 BERT & NLP Analysis

Natural Language Processing is used to analyze repository text and discover semantic relationships.

The project uses BERT-based embeddings to represent repository information in a numerical vector space.

These embeddings allow the system to compare repositories based on their semantic meaning rather than relying only on exact keyword matches.

---

## 🔍 Repository Similarity

The project includes a semantic similarity search based on the generated embeddings.

Similarity is calculated using **Cosine Similarity**.

Conceptually:

```text
Repository
     ↓
BERT Embedding
     ↓
Vector Representation
     ↓
Cosine Similarity
     ↓
Most Similar Repositories
```

This makes it possible to find repositories that are semantically similar even when their names or keywords are different.

---

## 🧠 Repository Classification

The project also includes a BERT-based repository classification component.

The classification results are used to categorize repositories into different technical areas.

Example categories include:

- Cybersecurity or Security Tools
- Machine Learning or Artificial Intelligence
- Data Science or Data Analytics
- Desktop Application Development
- Mobile Application Development
- Other technical categories

The classification results are visualized in the dashboard.

---

## 📊 Interactive Dashboard

The project includes an interactive dashboard built with **Streamlit**.

The dashboard provides several sections:

### 🏠 Dashboard

Provides an overview of the analyzed repositories, including:

- Number of repositories
- Number of association rules
- Top PageRank score
- Average stars
- Top repositories
- Repository category distribution

### 📈 PageRank

Displays repository ranking based on PageRank scores.

### 🔗 Association Rules

Explores the relationships discovered between repository topics.

### 🤖 BERT

Provides repository classification and semantic similarity functionality.

### 🌐 HITS

Displays hub and authority analysis.

---

## 📁 Project Structure

```text
GitHub-Repository-Mining/
│
├── app/
│   └── app.py
│
├── data/
│   └── sample_data.csv
│
├── models/
│   ├── embeddings.npy
│   └── graph.pkl
│
├── notebooks/
│   └── MiningGithub.ipynb
│
├── results/
│   ├── association_rules.csv
│   ├── authorities.csv
│   ├── bert_data.csv
│   ├── classification_results.csv
│   ├── hubs.csv
│   ├── pagerank_results.csv
│   └── rules (1).csv
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation |
| NumPy | Numerical computation |
| Scikit-learn | Machine learning and similarity |
| Matplotlib | Data visualization |
| Plotly | Interactive visualization |
| Streamlit | Interactive dashboard |
| BERT | NLP and semantic embeddings |
| NetworkX | Graph analysis |
| FP-Growth | Association rule mining |
| Jupyter Notebook | Data analysis and experimentation |

---

## ⚙️ Main Components

The project consists of several major components:

```text
GitHub Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Engineering
      │
      ├───────────────┐
      ▼               ▼
Graph Mining       NLP Analysis
      │               │
      ├── PageRank    ├── BERT
      │               ├── Classification
      ├── HITS        └── Similarity
      │
      ▼
Association Rule Mining
      │
      ▼
Results
      │
      ▼
Streamlit Dashboard
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd GitHub-Repository-Mining
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard

```bash
streamlit run app/app.py
```

The dashboard will open in your browser.

---

## 📌 Key Results

The current analysis contains:

| Metric | Value |
|---|---:|
| Analyzed Repositories | 3,000 |
| Association Rules | 72 |
| Top PageRank Score | 0.0039 |
| Average Stars | 14,287 |

The project combines graph analysis, data mining, and NLP to provide multiple perspectives for understanding GitHub repositories.

---

## 🚀 Future Improvements

Possible future improvements include:

- Increasing the dataset size.
- Adding more repository metadata.
- Improving classification performance.
- Adding more NLP models.
- Building advanced repository recommendation features.
- Adding temporal analysis to track repository popularity over time.
- Deploying the Streamlit dashboard online.
- Adding more interactive visualizations.

---

## 👩‍💻 Author

**Dai Gebril**

Data Science Student passionate about **Data Engineering, Data Mining, and Backend Development**.
⭐ If you find this project interesting, feel free to explore the repository!