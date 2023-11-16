#  PITA - Penn State Information Technology Advisor


## Product Description
PITA is a chatbot for the Penn State Abington IT Student Workers to utilize when they are faced with an issue they can not solve and need additional assistance with troubleshooting for common IT issues. This chatbot will enable the IT student workers to quickly retrieve answers to help faculty and students in an efficient manner. PITA answers common IT issues and questions, looks up details in the knowledge base, and provides step by step solutions. PITA serves as a fast and personalized virtual IT assistant. The chatbot provides an intuitive conversational interface for users to get help with troubleshooting, university software, and other technical problems.

The key goals for the PITA chatbot project include:
- Create an intuitive text-based conversational interface
- Allow IT staff to easily find answers to common support questions
- Reduce IT response times and enhance user satisfaction
- Develop a robust knowledge base for the chatbot from existing documents
- Provide high-quality conversational experiences powered by AI
- Deliver a minimum viable product that adds value for the IT department
- Establish a platform that can be expanded with more capabilities over time



## Documentation
- **Developer Guidelines**: [Developer Guidelines](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/DeveloperGuidelines.md)
- **User Manual**: [User Manual](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/UserManual.md)
- **Living Doc**: [Living Doc](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/LivingDoc)




## Use Cases
Operational Use Cases
- Resource for IT student workers when presented with questions beyond their technical knowledge
  - IT student workers can open the chatbot and ask it questions about Abington’s Information Technology Department and receive answers to better assist faculty.

Non-Operational Use Cases
- IT admins to determine if more training is necessary
- Removing outdated data from the IT department database
- Adding new information to the IT department database
- IT department to keep track of common technical issues
- Authenticating user IT admin
  - In order for these use cases to be operational, we need to implement a login system, which we are currently working on in addition to implementing a way to store user queries so IT admin can view the overall history as well as each student’s previously asked questions.  





## Getting Started
1. Navigate to our repository at https://github.com/Gabi-Gindoff/PITA-repository/tree/main
2. Open Codespaces by pressing the “.” key on your keyboard. When the codespaces opens, go to the three horizontal lines, select terminal, new terminal. Select “continue working in GitHub codespaces” and then select whichever instance type you want for your codespace (doesn’t matter if you choose 2 or 4 cores). You can now use the terminal to build, test, and run the program.   


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

 

## Team Info
- Gabriella Gindoff: Backend Engineer
- Adam Christopher: Frontend Engineer
- Harkaren Kaur: UI Design/ Frontend Engineer
- Treasure Davis: UI Design/ Frontend Engineer
- Elizabeth Johney: Backend Engineer
- Katherine Banis: Backend Engineer

