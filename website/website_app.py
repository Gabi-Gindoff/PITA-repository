from flask import Flask, render_template, request, jsonify


import torch




app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat2.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg

    chatbot_response = msg
    
    return chatbot_response




if __name__ == '__main__':
    app.run()
