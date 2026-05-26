import re
# Hinglish sentiment dictionary

hinglish_sentiment_map = {

    "bekar": "bad",
    "bakwas": "terrible",
    "ghatiya": "worst",
    "mast": "awesome",
    "badiya": "good",
    "accha": "good",
    "acha": "good",
    "kharab": "bad",
    "wahiyat": "terrible",
    "faadu": "amazing",
    "jhakas": "awesome",
    "zabardast": "excellent",
    "bekaar": "bad",
    "sahi": "good",
    "dangerous": "awesome",
    "lajawab": "excellent",
    "boring": "boring",
    "faltu": "useless",
    "paisa vasool": "worthwhile"
}


# Cleaning function

def clean_text(text):

    # Convert to lowercase
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)

    # Remove special characters but KEEP spaces
    text = re.sub(r'[^a-zA-Z!?.,\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Replace Hinglish sentiment words

    for hinglish_word, english_word in hinglish_sentiment_map.items():

       text = text.replace(
         hinglish_word,
        english_word
    )

    return text



# Test the function

if __name__ == "__main__":

    sample_text = "OMG!!! DHURANDHAR is soooo gooood 😍🔥"

    cleaned = clean_text(sample_text)

    print("\nOriginal Text:")
    print(sample_text)

    print("\nCleaned Text:")
    print(cleaned)