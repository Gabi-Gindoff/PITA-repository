# User Manual


## Table of Contents
- [High Level Description](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/UserManual.md#high-level-description-of-system)
- [How to Install Software](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/UserManual.md#how-to-install-software)
- [How to Run Software](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/UserManual.md#how-to-run-software)
- [How to Use Software](https://github.com/Gabi-Gindoff/PITA-repository/blob/main/Docs/UserManual.md#how-to-use-software)



## High Level Description of System

PITA (Penn State Information Technology Advisor) is an innovative chatbot meticulously crafted to empower IT student workers at Penn State Abington with efficient troubleshooting capabilities. Serving as a virtual IT assistant, PITA utilizes an intuitive conversational interface to promptly address common IT issues and provide step-by-step solutions. The chatbot's core objectives include reducing IT response times, enhancing user satisfaction, and establishing a robust knowledge base from existing documents. With a focus on user-friendly interactions and leveraging AI-driven conversational experiences, PITA aims to deliver a minimum viable product that significantly adds value to the IT department, ensuring adaptability and expansion over time.


PITA is built on a technological stack that synergizes the collaborative power of GitHub, the web development capabilities of Flask, the conversational intelligence of DialoGPT, and the efficient data management offered by SQLite. This integrated technology stack ensures PITA's effectiveness in delivering intuitive and responsive IT support for both IT student workers and end-users at Penn State Abington.


## How to Install Software
- **Step 1:** Navigate to our repository at https://github.com/Gabi-Gindoff/PITA-repository/tree/main
- **Step 2:** Open Codespaces by pressing the “.” key on your keyboard.
- **Step 3:** When the codespace opens, go to the three horizontal lines, select terminal, new terminal.
- **Step 4:** Select “continue working in GitHub codespaces”
- **Step 5:** A drop down menu should appear at the top of your screen, select either option for your codespace (doesn’t matter if you choose 2 or 4 cores).
- **Step 6:** You can now use the terminal to run the program, follow the directions below to run the software.

## How to Run Software
Note: in order to run the software you have to have poetry installed - you can skip the following if you already have poetry installed
```bash
  cd flask_db_app
  pip install poetry
  poetry install
```

Copy and paste the following code into the terminal to run the software: (
```bash
  cd flask_db_app
  poetry run python app.py
```
To access the website, click either the pop-up that appears in the bottom right or click the link directly from the terminal.
Doing either of these options will open up a new tab in your browser that you can interact with.
- **Press the keys "Crtl + C" in the terminal to exit the application at any time**


## How to Use Software

### As an IT Student Worker
- **Step 1:** Enter your user ID (any integer) into the User ID textbox, then press 'User Login'.
<img width="384" alt="image" src="https://github.com/Gabi-Gindoff/PITA-repository/assets/144366612/57bb386b-2102-4036-b146-77cf00f3bba2">

- **Step 2:** Type your question and click the "Enter" key or the arrow sign to ask the chatbot.  
<img width="542" alt="image" src="https://github.com/Gabi-Gindoff/PITA-repository/assets/144366612/366d29dd-c519-44b3-b48d-187a0a781250">

### As an IT Admin
- **Step 1:** Enter the adimin password (admin_password) into the Admin Password textbox, then press 'Admin Login'.
<img width="373" alt="image" src="https://github.com/Gabi-Gindoff/PITA-repository/assets/144366612/89a29d07-5400-48aa-9946-8ca78ce61e80">

- **Step 2:** Enter the User ID for the student whose history you want to view and hit 'Get Chat Logs'.
  <img width="429" alt="image" src="https://github.com/Gabi-Gindoff/PITA-repository/assets/144366612/0dbcc2f5-f7ea-461f-85c7-4efc2d4de06c">

- **Step 3:** Now you can view that users history
<img width="801" alt="image" src="https://github.com/Gabi-Gindoff/PITA-repository/assets/144366612/0e847d26-b33d-4ef1-8259-50ae0490c7cf">