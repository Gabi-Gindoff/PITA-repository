# Developer Guidelines

## Repo Structure
Main Branch 
- Docs: hosts our userManual,  developerGuidelines, and livingDoc files
- WeeklyReports: hosts our weekly updates and progress reports
- Flask_db_app: hosts all files necessary for the website, our database and our chatbot, as well as the connections between each


## How to Add a New Test Case



## Machine Prerequisites
Runs using ubuntu linux (can be run on any computer if using codespaces)

Step 1: Open Codespace
1. Navigate to our repo at https://github.com/Gabi-Gindoff/PITA-repository/tree/main
2. Press the “.” key on your keyboard
3. When the codespaces opens, go to the three horizontal lines, select terminal, new terminal.
4. Select “continue working in GitHub codespaces” and then select whichever instance type you want for your codespace (doesn’t matter if you choose 2 or 4 cores).
5. You can now use the terminal to build, test, and run the program.   


## How to Build the Software
1. Once you have a new terminal opened (using the steps above), you can proceed to build the system. All of the following steps are to be done using this terminal.  
2. First, enter the command “cd flask_db_app” - changes the directory to where the poetry.toml file is installed
3. Next, “pip install poetry” - this command installs poetry to be able to run the poetry install command.
4. Lastly, “poetry install” - this command downloads all the dependencies from the poetry.lock file.

## How to Test the Software
1. Before testing the system, ensure all the steps from the build system instruction are completed. Once the build is complete, you can proceed to testing. 
2. Ensure you are also in the “flask_db_app” directory, if not you can change it via the “cd flask_db_app” command. If you ever need to go back, you can use the “cd ..” command. 
3. Next, use the command “poetry run pytest test_app.py” to test the system
4. The terminal will display the tests as well as if they have passed or failed.
6. You can also run “python dapp.py” to see all the data currently in the database. In order to run this command, you have to do "pip install -r requirements.txt"
7. Then, at the bottom of the page, you can use the form to add a row into the database. For the category, put “Testing” so we can easily remove it from the database - you can now view the query on the previous page 
8. To delete the query, go back to the terminal, hit ctrl c to close the port, and run “python delete_test_from_db.py” 
9. Now when you run  “python dapp.py” again, you will not see the query that was just added and then deleted.
10. Go back to the terminal and hit “ctrl c” to close the application


## How To Run the Software
1. First, ensure that you are in the “flask_db_app” directory, if not you can change it via the “cd flask_db_app” command.
2. To run the system after building it, enter “poetry run python app.py” to run the application. A pop-up should appear that prompts you to open the port in a new browser, if not, the link for the webpage with the chatbot will be in the terminal.
3. Ask the chatbot a question like “Where are the printers located?” and see what it says. 
4. To exit the application and kill the port, press the keys Ctrl + C on your keyboard.
5. Note: you can also run the system with "python app.py" if you did the "pip install -r requirements.txt"


## CI Setup & Viewing Build History 
Our CI can be found in the .github/workflows folder


