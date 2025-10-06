import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources (only the first time)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

class TextCleaner:
    def __init__(self, remove_stopwords=True, lemmatize=True, remove_fillers=True):
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize
        self.remove_fillers = remove_fillers

        # Load stopwords and lemmatizer
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

        # Common filler words (you can add more)
        self.fillers = {"uh", "um", "like", "you know", "so", "actually", "basically"}

    def clean_text(self, text):
        """Clean and preprocess raw text input."""

        # 1️⃣ Lowercasing
        text = text.lower()

        # 2️⃣ Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # 3️⃣ Tokenize (split into words)
        tokens = text.split()

        # 4️⃣ Remove filler words
        if self.remove_fillers:
            tokens = [t for t in tokens if t not in self.fillers]

        # 5️⃣ Remove stopwords
        if self.remove_stopwords:
            tokens = [t for t in tokens if t not in self.stop_words]

        # 6️⃣ Lemmatize words
        if self.lemmatize:
            tokens = [self.lemmatizer.lemmatize(t) for t in tokens]

        # 7️⃣ Return cleaned text
        return ' '.join(tokens)


# ---------- Example Run ----------
if __name__ == "__main__":
    cleaner = TextCleaner()

    sample_texts = [
        "Um, I think like this movie was actually really good!",
        "So basically, you know, the results are not that bad.",
        "Uh... the data looks messy, we need to clean it!"
    ]

    for text in sample_texts:
        print(f"Original: {text}")
        print(f"Cleaned : {cleaner.clean_text(text)}")
        print("-" * 60)
