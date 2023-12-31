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



## Repo Structure
Main Branch
- Docs: hosts our userManual and DevDocumentation files
- WeeklyReports: hosts our weekly updates and progress reports
- Flask_db_app: hosts all files necessary for the website and our database, as well as the connection between the two



## Use Cases
Operational Use Cases
- Resource for IT student workers when presented with questions beyond their technical knowledge
  - IT student workers can open the chatbot and ask it questions about Abington’s Information Technology Department and receive answers to better assist faculty.
- IT admins to determine if more training is necessary
  -  Admin can login to view user history in order to determine if students need more training to better support staff
- Authenticating user IT admin
  - Main admin password that can be used in order to view student chatbot history

Non-Operational Use Cases
- Removing outdated data from the IT department database
  - Can do this as a developer using the form when running dapp.py
- Adding new information to the IT department database
  - Can do this as a developer using the form when running dapp.py
- IT department to keep track of common technical issues
  - Wanted to implement an analysis page with common issues
   





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



## Technical Processes

Version control
- Our project is hosted on Github which comes with Git and is therefore handling our version control. We created a public repository named PITA-repository and have been utilizing the Codespaces within GitHub to run our program.
  - https://docs.github.com/en/get-started/using-git/about-git#about-version-control-and-git

Bug tracking
- We are using GitHub Issues for bug tracking. Our issues can be found by going to the issues tab within our repository ( https://github.com/Gabi-Gindoff/PITA-repository/issues). Using this tab we can add a new issue, comment on an ongoing issue, or close a fixed issue. We have been using two labels, for backend and frontend so each team knows what bugs they have to work on.
  - https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues

Build system
- We are using Poetry for our build system. In order to build the program, navigate to the codespaces using the above instructions and then use the step by step directions in the READ.me to install and run poetry.
  - https://python-poetry.org/docs/pyproject/

Testing
- We are using Pytest for our testing system. In order to test the program, navigate to the codespaces using the above instructions and then use the step by step directions in the READ.me to install and run Pytest.
  - https://docs.pytest.org/en/7.1.x/getting-started.html

CI
- We are using Github Actions for our continuous integration. To do this, we navigated to the actions tab within the repository ( https://github.com/Gabi-Gindoff/PITA-repository/actions) and created a new workflow. We wrote a new yml file that fit our needs for CI for this project. This file can be found by going to (PITA-repository/.github/workflows/mainCL.yml). This workflow named "CI Build" is triggered on both push events to the main branch and pull requests targeting the main branch. The workflow is designed to build, test, and set up our Python project.
  - https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration
 



## Documentation
- **Developer Guidelines**: [Developer Guidelines](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/DeveloperGuidelines.md)
- **User Manual**: [User Manual](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/UserManual.md)
- **Living Doc**: [Living Doc](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/LivingDoc)





## Team Info
- Gabriella Gindoff: Backend Engineer
- Adam Christopher: Frontend Engineer
- Harkaren Kaur: UI Design/ Frontend Engineer
- Treasure Davis: UI Design/ Frontend Engineer
- Elizabeth Johney: Backend Engineer
- Katherine Banis: Backend Engineer
