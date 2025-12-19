This project is an end-to-end sentiment analysis system trained on millions of Amazon product reviews and deployed as a Flask REST API.
The model predicts whether a given review is positive or negative.

Dataset: Amazon Review Polarity Dataset
Task: Binary sentiment classification (positive / negative)
Model: TF-IDF + Logistic Regression
Accuracy: ~91%
Deployment: Flask API
Language: Python

Size:
3.6M training samples
400K test samples

API Usage:

Endpoint
POST /predict

Request (JSON)
{
  "review": "This product is amazing, I love it!"
}

Response
{
  "sentiment": "Positive",
  "confidence": 0.94
}

Technologies Used:
Python
Pandas
Scikit-learn
TF-IDF
Logistic Regression
Flask
Joblib

Author : Emircan Akgül
