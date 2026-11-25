
# URL Phishing Detection System 🔐

## 📌 Project Overview

The URL Phishing Detection System is an AI/ML-based web application that identifies whether a given website URL is legitimate or potentially malicious.

The system extracts various features from URLs and uses Machine Learning classification to predict phishing websites.

## 🚀 Key Features

- Real-time URL classification
- Automated URL feature extraction
- Legitimate vs Phishing prediction
- Probability analysis for both classes
- Interactive Streamlit web interface
- Machine Learning-based detection

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Machine Learning

## 🧠 Machine Learning Approach

The project evaluates multiple classification algorithms:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest

Random Forest was selected based on the evaluation results.

**Reported F1-score: 0.7921**

## ⚙️ How It Works

1. User enters a website URL.
2. The system extracts relevant URL features.
3. Extracted features are processed by the trained model.
4. The model predicts whether the URL is legitimate or phishing.
5. The application displays the prediction and probability analysis.

## 📂 Project Structure

```text
URL-Phishing-Detection/
│
├── app.py
├── train_model.py
├── feature_extraction.py
├── test_features.py
├── feature_columns.pkl
├── model_info.pkl
├── scaler.pkl
├── vectorizer.pkl
│
├── dataset/
│   └── phishing_site_urls.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 💻 Installation and Execution

Clone the repository:

```bash
git clone https://github.com/Inshal-26/URL-Phishing-Detection.git
```

Navigate into the project:

```bash
cd URL-Phishing-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📊 Model Performance

The selected Random Forest model achieved an F1-score of **0.7921** in the reported evaluation.

## 🎯 Project Objective

To develop an interactive Machine Learning application that helps identify potentially fraudulent websites through URL-based feature analysis.

## 👩‍💻 Author

**Inshal**

GitHub: [Inshal-26](https://github.com/Inshal-26)

---

⭐ If you find this project interesting, consider giving the repository a star!
## Live Demo

Try the deployed application here:

[URL Phishing Detection System](https://url-phishing-detection-hrhagpza2zhcgjpe3arvsz.streamlit.app/)
