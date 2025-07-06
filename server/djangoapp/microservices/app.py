# from flask import Flask
# from nltk.sentiment import SentimentIntensityAnalyzer
# import json
# import os

# app = Flask("Sentiment Analyzer")

# sia = SentimentIntensityAnalyzer()


# @app.get('/')
# def home():
#     return "Welcome to the Sentiment Analyzer. \
#     Use /analyze/text to get the sentiment"


# @app.get('/analyze/<input_txt>')
# def analyze_sentiment(input_txt):

#     scores = sia.polarity_scores(input_txt)
#     print(scores)
#     pos = float(scores['pos'])
#     neg = float(scores['neg'])
#     neu = float(scores['neu'])
#     res = "positive"
#     print("pos neg nue ", pos, neg, neu)
#     if (neg > pos and neg > neu):
#         res = "negative"
#     elif (neu > neg and neu > pos):
#         res = "neutral"
#     res = json.dumps({"sentiment": res})
#     print(res)
#     return res

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/insert_review', methods=['POST'])
# def insert_review():
#     try:
#         review = request.get_json()
#         print("Received review:", review)
        
#         # Here, do any validation or storage logic you want
#         return jsonify({"message": "Review received"}), 200

#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": "Error inserting review"}), 500


# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import json

app = Flask("Sentiment Analyzer")
sia = SentimentIntensityAnalyzer()


@app.route('/')
def home():
    return "Welcome to the Sentiment Analyzer. Use /analyze or /insert_review"


@app.route('/analyze/<input_txt>', methods=['GET'])
def analyze_sentiment(input_txt):
    scores = sia.polarity_scores(input_txt)
    pos = scores['pos']
    neg = scores['neg']
    neu = scores['neu']
    
    if neg > pos and neg > neu:
        sentiment = "negative"
    elif neu > pos and neu > neg:
        sentiment = "neutral"
    else:
        sentiment = "positive"
    
    return jsonify({"sentiment": sentiment})


@app.route('/insert_review', methods=['POST'])
def insert_review():
    try:
        review = request.get_json()
        print("Received review:", review)

        # Validate input
        if "review" not in review:
            return jsonify({"error": "Missing review text"}), 400

        text = review["review"]
        scores = sia.polarity_scores(text)
        pos = scores['pos']
        neg = scores['neg']
        neu = scores['neu']

        if neg > pos and neg > neu:
            sentiment = "negative"
        elif neu > pos and neu > neg:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        return jsonify({"sentiment": sentiment}), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Error inserting review"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3030))  # You use 3030
    app.run(host="0.0.0.0", port=port)
