
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

data = pd.read_csv("dataset/phishing_site_urls.csv")

data = data.dropna(subset=["URL", "Label"])

data["URL"] = data["URL"].astype(str).str.strip()
data = data[data["URL"] != ""]

data["Label"] = data["Label"].map({
    "good": 0,
    "bad": 1
})

data = data.dropna(subset=["Label"])
data["Label"] = data["Label"].astype(int)

X = data["URL"]
y = data["Label"]

print("Dataset shape:", data.shape)

print("\nLabel distribution:")
print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(3, 5),
    min_df=2,
    max_features=100000,
    sublinear_tf=True,
    dtype="float32"
)

print("\nConverting URLs into TF-IDF features...")

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(
    max_iter=500,
    class_weight="balanced",
    random_state=42
)

print("\nTraining Logistic Regression...")

model.fit(X_train_tfidf, y_train)

print("\nEvaluating model...")

y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n========== MODEL PERFORMANCE ==========")

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

print("\n========== CLASSIFICATION REPORT ==========")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Legitimate", "Phishing"]
    )
)

print("\n========== CONFUSION MATRIX ==========")

cm = confusion_matrix(y_test, y_pred)

print(cm)

print("\n========== SAVING MODEL ==========")

model_info = {
    "model": model,
    "model_name": "TF-IDF + Logistic Regression",
    "uses_scaler": False,
    "uses_tfidf": True
}

joblib.dump(model_info, "model_info.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel saved successfully.")
print("Model: model_info.pkl")
print("Vectorizer: vectorizer.pkl")
