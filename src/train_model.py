import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_output.csv")
print(df[['text', 'cleaned_text', 'sentiment']].head(10))


# Label Mapping

print("\nLabel Mapping:\n")
print(df[['sentiment', 'label']].drop_duplicates())


# Features and Lables

X = df['cleaned_text']
y = df['label']


# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TF-IDF

vectorizer = TfidfVectorizer(
    max_features=8000,
    ngram_range=(1, 2)
)

# Fit transform
X_train_vec = vectorizer.fit_transform(X_train)

# Transform test
X_test_vec = vectorizer.transform(X_test)

print("\nVectorization completed.")


# Model

model = LogisticRegression(
    max_iter=1000
)

# Fit transform
X_train_vec = vectorizer.fit_transform(X_train)

# Transform test
X_test_vec = vectorizer.transform(X_test)

print("\nVectorization completed.")


# Model

model = LogisticRegression(
    max_iter=1000
)

# Train
model.fit(X_train_vec, y_train)

print("Model training completed.")


# Predict

y_pred = model.predict(X_test_vec)


# Evaluation

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# Save Vectorizer

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)


# Save Model

with open("models/logistic_regression_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel and vectorizer saved successfully!")