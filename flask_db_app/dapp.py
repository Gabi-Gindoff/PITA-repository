from flask import Flask, render_template, request, redirect, url_for

import sqlite3

app = Flask(__name__)

@app.route('/')
def display_data():
    # Connect to the database
    conn = sqlite3.connect('it_Department')
    cursor = conn.cursor()

    # Query the data
    #cursor.execute("SELECT name, age FROM my_table")
    cursor.execute('SELECT * FROM HelpDeskTickets')
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    # Pass the data to the template
    return render_template('data.html', data=data)

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        question = request.form['question']
        response = request.form['response']
        responseDate = request.form['responseDate']
        category = request.form['category']

        # Connect to the SQLite database
        conn = sqlite3.connect('it_Department')
        cursor = conn.cursor()

        # Insert the submitted data into the HelpDeskTickets table
        cursor.execute("INSERT INTO HelpDeskTickets (question, response, responseDate, category) VALUES (?, ?, ?, ?)",
                       (question, response, responseDate, category))


        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return redirect(url_for('display_data'))  # Redirect to display the updated data

    return render_template('add_data.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
