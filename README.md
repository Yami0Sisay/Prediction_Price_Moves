# Predicting Stock Price Movements Using News Sentiment  
10 Academy – AI Mastery | Week 1 Challenge

## Project Overview
This project explores whether **news sentiment** can be used to predict **stock market movements**.  
Over three tasks, I performed:

1. **Exploratory Data Analysis (EDA)** on financial news  
2. **Technical indicator computation** using TA-Lib + stock analysis  
3. **Correlation study between headline sentiment and stock returns**

The goal is to build a reproducible and modular pipeline for analyzing financial news and market data.

---

## How to Run This Project

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd <repo-name>
```
### 2. Create & Activate Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Notebooks

Open Jupyter or VSCode and run any notebook inside /notebooks.

## Task Summaries
### Task 1: News EDA

Explored text length, keywords, and n-grams

Publication trends over time

Publisher frequency + email domain extraction

Time-of-day and day-of-week patterns

Cleaned dataset for sentiment analysis

#### Key Outputs:

EDA plots

Cleaned news dataset

Feature engineering (headline length, cleaned text)

### Task 2: Stock Analysis

Downloaded stock data using yfinance

Cleaned and flattened OHLCV MultiIndex

Computed technical indicators using TA-Lib:

SMA

EMA

RSI

MACD

Basic financial metrics (returns, volatility)

Visualized indicators vs price movements

#### Key Outputs:

Technical indicators

TA-Lib–based analysis

Stock price visualizations

### Task 3: Sentiment–Market Correlation

Performed TextBlob sentiment analysis on headlines

Aggregated sentiment scores per day

Downloaded multi-ticker stock data

AAPL

GOOG

MSFT

NVDA

Computed daily returns

Merged news sentiment with stock returns

Calculated Pearson correlations

Visualized sentiment vs return scatterplots

#### Key Outputs:

Daily average sentiment

Multi-stock daily returns

Correlation results per ticker

## Modular Code (src/ folder)
```bash
src/data_loader.py
```
Loads and cleans news dataset.
```bash
src/sentiment.py
```
Computes polarity + sentiment categories.
```bash
src/stock.py
```
Downloads and cleans stock OHLCV data.
```bash
src/correlation.py
```
Joins sentiment and returns + computes correlations.

This modular structure satisfies Week 1's requirement for reusable and maintainable code.

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:

installs dependencies

runs tests (if provided)

ensures clean notebook execution

This ensures reproducibility and aligns with Week 1 scoring criteria.



## 📂 Folder Structure
```bash
PREDICTION_PRICE_MOVES/
│
├── .github/
│   └── workflows/
│       └── Ci.yml
│
├── .vscode/
│   └── settings.json
│
├── data/
│
├── notebooks/
│   ├── __init__.py
│   ├── news_eda.ipynb
│   ├── news_stock.ipynb
│   ├── quantitaive_analysis.ipynb
│   └── README.md
│
├── scripts/
│   ├── __init__.py
│   └── README.md
│
├── src/
│   ├── data_loader.py
│   ├── sentiment.py
│   ├── stock.py
│   ├── correlation.py
│   └── __init__.py
│
├── tests/
│   └── __init__.py
│
├── .gitignore
├── README.md 
└── requirements.txt
```
