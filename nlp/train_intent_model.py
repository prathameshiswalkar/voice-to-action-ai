import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

# dataset
df = pd.read_csv(r"D:\voice-agent-ai\data\dataset.csv")

x = df['text']
y = df['intent']

# pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(
        ngram_range=(1, 2), lowercase=True)),
    ('clf', LogisticRegression(max_iter=1000))
])

# Training model 
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y)

pipeline.fit(x_train, y_train) 

# Evaluating model
pred = pipeline.predict(x_test)
accuracy = accuracy_score(y_test, pred)

# SAVE MODEL
with open("models/intent_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)


# print("Intent Accuracy:", accuracy)
# print(df["intent"].value_counts())

# scores = cross_val_score(pipeline, x, y, cv= 3)
# print("CV Accuracy: ",scores.mean())

