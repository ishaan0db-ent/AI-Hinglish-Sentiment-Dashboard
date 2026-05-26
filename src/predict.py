import pickle

from preprocessing import clean_text

# Load vectorizer
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load trained model
with open("models/linear_svc_model.pkl", "rb") as f:
    model = pickle.load(f)

# Label mapping
label_map = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}

def predict_sentiment(text):

    # Clean input text
    cleaned_text = clean_text(text)

    # Convert text into vector
    vectorized_text = vectorizer.transform([cleaned_text])

    # Predict sentiment
    prediction = model.predict(vectorized_text)[0]

    # Return readable label
    return label_map[prediction]


# Test Input
sample_text = "OMG!!! DHURANDHAR is soooo gooood"

# Predict
result = predict_sentiment(sample_text)

# Output
print("\nInput Text:")
print(sample_text)

print("\nPredicted Sentiment:")
print(result)