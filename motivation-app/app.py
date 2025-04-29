from flask import Flask, jsonify, send_from_directory, request
import random
import os

app = Flask(__name__, static_folder='.', static_url_path='')

quotes = {
    "happy": [
        "Happiness is not by chance, but by choice 😊.",
        "The purpose of our lives is to be happy 😄."
    ],
    "sad": [
        "Sadness flies away on the wings of time 💙.",
        "Even the darkest night will end and the sun will rise 🌅."
    ],
    "stressed": [
        "In the middle of difficulty lies opportunity 💡.",
        "Breathe. It's just a bad day, not a bad life 🌬️."
    ],
    "motivated": [
        "Push yourself, because no one else is going to do it for you 💪.",
        "Great things never come from comfort zones 🚀."
    ]
}

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/quote.html')
def serve_quote():
    return send_from_directory('.', 'quote.html')

@app.route('/get_quote/<mood>')
def get_quote(mood):
    mood = mood.lower()
    if mood in quotes:
        return jsonify({'quote': random.choice(quotes[mood])})
    else:
        return jsonify({'quote': 'Sorry, no quotes available for that mood.'})

if __name__ == '__main__':
    app.run(debug=True)  