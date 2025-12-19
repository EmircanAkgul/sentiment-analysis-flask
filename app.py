from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "comment" not in data:
        return jsonify({"error": "comment alanı gerekli"}), 400

    text = data["comment"]

    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X).max()

    sentiment = "positive" if pred == 1 else "negative"

    return jsonify({
        "sentiment": sentiment,
        "confidence": round(float(prob), 3)
    })

if __name__ == "__main__":
    app.run(debug=False)
