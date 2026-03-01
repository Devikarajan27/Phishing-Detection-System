from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("phishing_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    legit_percent = 0
    phish_percent = 0

    if request.method == "POST":
        url = request.form["url"]

        # TEMPORARY: generate random features (until we build real extraction)
        sample = np.random.randint(-1, 2, 30).reshape(1, -1)

        prediction = model.predict(sample)[0]
        probabilities = model.predict_proba(sample)[0]

        legit_percent = round(probabilities[1] * 100, 2)
        phish_percent = round(probabilities[0] * 100, 2)

        if prediction == 1:
            result = "Legitimate Website"
        else:
            result = "Phishing Website"

    return render_template("index.html",
                           result=result,
                           legit=legit_percent,
                           phish=phish_percent)

if __name__ == "__main__":
    app.run(debug=True)