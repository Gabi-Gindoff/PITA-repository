# User Manual

## High Level Description of the System

## Instructions for Using System

Step 1: Click on the interactive text box

Step 2: Type your question and click enter or the arrow sign to ask the chatbot.

Step 3: Chatbot will display your answered question, you can repeat these steps as many times as needed.


## How to Build the System
Once you have a new terminal opened (using the steps above found in the getting started section), you can proceed to build the system. All of the following steps are to be done using this terminal.  
Copy and paste the following code into the terminal:
```bash
   cd flask_db_app
   pip install poetry
   poetry install
```

## How to Test the System
Before testing the system, ensure all the steps from the build system instruction are completed. Once the build is complete, you can proceed to testing. 
Copy and paste the following code into the terminal:

To test the application:
```
   bash
   cd flask_db_app
   poetry run pytest test_app.py
```
To see data in database:
```
  bash
  cd flask_db_app
  poetry run python dapp.py
```
To delete the new testing entry made by the testing command:
```
  bash
  cd flask_db_app
  python delete_test_from_db.py
```

**Press the keys "Crtl + C" in the terminal to exit the application at anytime**

  

## How to Run the System
Copy and paste the following code into the terminal:

To run the system:
```
  bash
  cd flask_db_app
  poetry run python app.py
```
To access the website, click either the pop-up that appears in the bottom right or click the link directly from the terminal.
Doing either of these options will open up a new tab in your browser that you can interact with.
**Press the keys "Crtl + C" in the terminal to exit the application at any time**
