from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def em_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    parts = [f"'{k}': {response[k]}" for k in emotion_keys]
    scores = ", ".join(parts[:-1]) + " and " + parts[-1]

    return (f"For the given statement, the system response is {scores}. "
            f"The dominant emotion is {response['dominant_emotion']}.")


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)