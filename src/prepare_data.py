import pandas as pd

from preprocessing import clean_text

# Load dataset
df = pd.read_csv("data/raw/output.csv")

# Clean text column
df['cleaned_text'] = df['text'].apply(clean_text)

# Save cleaned dataset
df.to_csv(
    "data/processed/cleaned_output.csv",
    index=False
)

print("Data preprocessing completed successfully!")