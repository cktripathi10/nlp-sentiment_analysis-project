# nlp-sentiment_analysis-project
A NLP project for tweet sentiment analysis using logistic regression, featuring data preprocessing, word frequency analysis, and model training/evaluation.

# Tweet Sentiment Analysis with Logistic Regression

This project demonstrates sentiment analysis on tweets using logistic regression, built as part of a Coursera NLP course.

## Overview
- **Goal**: Classify tweets as positive or negative.
- **Skills**: NLP preprocessing, feature extraction, logistic regression, Python (numpy, pandas, nltk, matplotlib).
- **Accuracy**: ~99.5% on test set.

## Files
- `preprocessing.ipynb`: Tokenizes and stems tweets.
- `word_frequencies.ipynb`: Builds and visualizes word frequencies.
- `logistic_regression_model.ipynb`: Visualizes the logistic regression model.
- `assignment_logistic_regression.ipynb`: Implements and tests the model.
- `utils.py`: Helper functions.
- `requirements.txt`: Dependencies.

## Setup
```bash
git clone https://github.com/cktripathi10/nlp-sentiment_analysis-project.git
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python -c "import nltk; nltk.download('twitter_samples'); nltk.download('stopwords')"
jupyter notebook

Results

Achieved 99.65% accuracy.
Example: "I am learning :)" → Positive sentiment (0.83).

Built by Chandan Tripathi for Coursera NLP Specialization.