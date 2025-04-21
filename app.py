from flask import Flask, render_template, request
from textblob import TextBlob
import pytesseract
from PIL import Image
import os

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Text Analysis Page
@app.route('/text-analysis', methods=['GET', 'POST'])
def text_analysis():
    sentiment = None
    if request.method == 'POST':
        review = request.form['review']
        analysis = TextBlob(review)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
    return render_template('text_analysis.html', sentiment=sentiment)

# Image Analysis Page
@app.route('/image-analysis', methods=['GET', 'POST'])
def image_analysis():
    sentiment = None
    extracted_text = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('image_analysis.html', error='No file part')
        file = request.files['image']
        if file.filename == '':
            return render_template('image_analysis.html', error='No selected file')
        if file:
            image = Image.open(file.stream)
            extracted_text = pytesseract.image_to_string(image)
            analysis = TextBlob(extracted_text)
            polarity = analysis.sentiment.polarity
            if polarity > 0:
                sentiment = 'Positive'
            elif polarity < 0:
                sentiment = 'Negative'
            else:
                sentiment = 'Neutral'
    return render_template('image_analysis.html', sentiment=sentiment, extracted_text=extracted_text)

# Movie Review Analysis Page
@app.route('/movie-review', methods=['GET', 'POST'])
def movie_review():
    sentiment = None
    if request.method == 'POST':
        review = request.form['review']
        analysis = TextBlob(review)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
    return render_template('movie_review.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)