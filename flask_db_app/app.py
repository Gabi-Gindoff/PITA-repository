from flask import Flask, render_template, request, jsonify


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

import sqlite3

from flask import Flask, render_template, request, jsonify
from dapp import app as database_app  # Import your "dapp.py" application

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat2.html')

@app.route('/get', methods=['POST'])
def chat():
    msg = request.form['msg']
    response = get_chat_response(msg)
    return response

from difflib import SequenceMatcher

def get_chat_response(user_input):
    conn = sqlite3.connect('it_Department')  # Connect to the existing database
    cursor = conn.cursor()

    # Get the data from the HelpDeskTickets table
    cursor.execute('SELECT question, response FROM HelpDeskTickets')
    saved_responses = cursor.fetchall()

    best_score = 0
    matched_response = "Sorry, I don't have a response to that."

    # Iterate through the saved responses and find the most similar match for the user's input
    for question, response in saved_responses:
        similarity = SequenceMatcher(None, question.lower(), user_input.lower()).ratio()
        if similarity > best_score:
            best_score = similarity
            matched_response = response

    conn.close()

    # Set a similarity threshold, below which it might not be considered a match
    if best_score < 0.5:
        return "Sorry, I don't have a response to that."
    else:
        return matched_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Run the chatbot app on a different port than the dapp.py
