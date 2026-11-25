
# URL Phishing Detection System

## Overview
An AI/ML-based web application that detects whether a given URL is legitimate or phishing.

## Features
- URL-based phishing detection
- Automated URL feature extraction
- Machine learning prediction
- Legitimate and phishing probability analysis
- Interactive Streamlit interface

## Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Machine Learning

## Machine Learning
The project uses multiple machine learning algorithms and selects a model based on evaluation metrics.

## Project Structure
- app.py
- train_model.py
- feature_extraction.py
- test_features.py
- feature_columns.pkl
- model_info.pkl
- scaler.pkl
- vectorizer.pkl
- dataset/phishing_site_urls.csv
- requirements.txt

## Installation

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd URL_Phishing_Detection_Project
pip install -r requirements.txt
streamlit run app.py
```

## Author
Inshal
