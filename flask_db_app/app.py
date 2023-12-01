from flask import Flask, render_template, request, jsonify, redirect, url_for, session


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from difflib import SequenceMatcher

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

#tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-step-50K-105b")
#model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-step-50K-105b")

import sqlite3

#from flask import Flask, render_template, request, jsonify
from dapp import app as database_app  # Import your "dapp.py" application
from transformers import AutoModelForCausalLM, AutoTokenizer

#from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Add your secret key
app.config['PROPAGATE_EXCEPTIONS'] = True

# Route for root URL - direct to login
@app.route('/')
def index():
    return render_template('login.html')


# Route for user login
@app.route('/user_login', methods=['POST'])
def user_login():
    user_id = request.form['user_id']
    
    # Here, you can perform any desired authentication or simply save the user ID in the session
    session['user_id'] = user_id  # Save the user ID in the session
    
    # Redirect to the chat interface regardless of the user ID
    return redirect(url_for('chat_interface', user_id=user_id))

# Route for admin login
@app.route('/admin_login', methods=['POST'])
def admin_login():
    password = request.form['password']
    # Check if the password is correct (you should use a secure method here)
    if password == 'admin_password':
        # For demonstration purposes, save the admin status in the session
        session['is_admin'] = True
        return redirect(url_for('admin_interface'))
    else:
        return "Invalid password. Please try again."
# Route for the chat interface
@app.route('/chat/<user_id>')
def chat_interface(user_id):
    # Check if the user is logged in
    if 'user_id' in session and session['user_id'] == user_id:
        return render_template('chat.html', user_id=user_id)
    else:
        return "Unauthorized Access."
# Route for the admin interface
@app.route('/admin_interface')
def admin_interface():
    # Check if the user is an admin
    if 'is_admin' in session and session['is_admin']:
        return render_template('admin_view.html')
    else:
        return "Unauthorized Access."
# ... (other routes, functions, and logic)

# ... (other configurations and routes)

@app.route('/get', methods=['POST'])
def chat():
    msg = request.form['msg']
    response = get_chat_response(msg)
    return response


def get_chat_response(user_input):
    conn = sqlite3.connect('it_Department')  # Connect to the existing database
    cursor = conn.cursor()
    # Get the data from the HelpDeskTickets table
    cursor.execute('SELECT question, response FROM HelpDeskTickets')
    saved_responses = cursor.fetchall()
    best_score = 0
    matched_response = "I don't have an answer to that, you may find your answer here: https://www.it.psu.edu/services/"
    # Iterate through the saved responses and find the most similar match for the user's input
    for question, response in saved_responses:
        similarity = SequenceMatcher(None, question.lower(), user_input.lower()).ratio()
        if similarity > best_score:
            best_score = similarity
            matched_response = response
    conn.close()
    # Set a similarity threshold, below which it might not be considered a match
    if best_score < 0.4:
        return "I don't have an answer to that, you may find your answer here: https://www.it.psu.edu/services/"
    else:
        return matched_response


# Set up SQLite database connection
conn = sqlite3.connect('chat_logs.db')
# Set up SQLite database connection
def create_chat_log_table(user_id):
    conn = sqlite3.connect('chat_logs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ChatLogs (
            id INTEGER PRIMARY KEY,
            user_id TEXT,
            message TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()  # Commit changes to the database
    conn.close()

# ... (other routes and login logic)
@app.route('/admin_view', methods=['GET', 'POST'])
def admin_view():
    if request.method == 'POST':
        user_id = request.form['user_id']
        #conn = sqlite3.connect(f'/{user_id}_chat_logs.db')
        conn = sqlite3.connect('chat_logs.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ChatLogs WHERE user_id = ?', (user_id,))
        #cursor.execute('SELECT * FROM ChatLogs')
        logs = cursor.fetchall()
        conn.close()
        return render_template('admin_view.html', logs=logs, user_id=user_id)
    return render_template('admin_view.html')




@app.route('/save_chat_log', methods=['POST'])
def save_chat_log():
    if request.method == 'POST':
       # try:
        user_id = request.form['user_id']
        question = request.form['question']
        timestamp = request.form['timestamp']
        
        create_chat_log_table(user_id)  # Create the table if it doesn't exist
        #conn = sqlite3.connect(f'/{user_id}_chat_logs.db')
        conn = sqlite3.connect('chat_logs.db')
        cursor = conn.cursor()
        # Insert the chat log into the ChatLogs table for the specific user ID
        cursor.execute('INSERT INTO ChatLogs (user_id, message, timestamp) VALUES (?, ?, ?)', (user_id, question, timestamp))
        conn.commit()
        conn.close()
        return "Chat log saved successfully!"
       # except Exception as e:
       #     app.logger.error("An error occurred: %s", str(e), exc_info=True)
       #     return "An error occurred while saving the chat log.", 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Run the chatbot app on a different port than the dapp.py
