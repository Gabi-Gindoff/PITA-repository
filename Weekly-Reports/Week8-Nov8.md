# Team Report & Updates
  - ### Last Week’s Goals:
      -  Last week Adam and Gabi worked on setting up a flask connection to our database. After multiple failed attempts, we finally got it set up with a sqlite database with the helpDeskTickets and a flask app which is used for testing right now. We also worked on creating and running pytests. We were able to check these tests visually using the flask app to ensure we can read, insert, and delete from the database. We also worked on creating a yaml file for our CI assignment. Everything builds except running the flask app. We tried adding a script to close the flask app once it opens successfully but it did not work. Going to continue working on this to try to get it all to pass successfully.
  - ### This Week's Progress & Issues:
      -  Treasure got the website working and connected to the dialoGPT model. It is now connected to our database and when you ask it a question that resembles a question that is found in the database, it will return a response. At first it didn't work in codespaces but the three of us got together and got it to work by compiling all the code needed for both the website and the database into one folder. Need to work on the fallback mechanism as right now it will just say "Sorry I don’t have a response for that" for questions beyond the scope of the current database. 
  - ### Next Week’s Plan:
      -  Adam and Gabi are going to work on implementing a build system using poetry and work on fixing our CI pipeline so that it builds properly. Katherine will work on adding more tests using pytests and Elizabeth will work on getting more data from the IT channel. Treasure and Karen and going to work on making the website more aesthetically pleasing and user friendly.

# Contributions of individual team members
  - ### Gabriella:
      - Last Week’s Goals:
          -  Last week I worked on setting up our database with Flask. I followed tutorials about setting up the connection (askpython) and watched lectures/videos on cs50 flask (harvard) recommended by Professor Wagenhoffer. First I tired connecting flask with the database that was hosted on my laptop on mysql server. Then I tried setting it up with XXAMP and PhpMyAdmin but there was a problem with the connection. With the professor's help, I was able to set up the connection between a sqlite database with flask using our repo's codespaces. I also worked with Adam to add and run pytests, and then set up our CI using GitHub Actions.
      - This Week's Progress & Issues:
          -  This week I met with Adam and Treasure to get the website to connect with the database. We successfully connected it all and have a working chatbot that pulls the responses from our database. Managed to get it working in codespaces. Cleaned up the repo by deleting all old files that were not being used.
      - Next Week’s Plan:
          -  Next week I plan on working on the documentation and getting ready for the alpha release. Going to work with Adam and Treasure to use poetry, pytest, and GitHub actions to get everything set up properly. If there is time possibly add the linter and coverage report. 
  
  - ### Adam:
      - Last Week’s Goals:
          -  ________________________________________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
        
  - ### Treasure:
      - Last Week’s Goals:
          -  ________________________________________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
          
  - ### Harkaren:
      - Last Week’s Goals:
          - _____________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
        
  - ### Elizabeth:
      - Last Week’s Goals:
          -  ________________________________________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
        
  - ### Katherine:
      - Last Week’s Goals:
          -  ________________________________________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
![image](https://github.com/Gabi-Gindoff/PITA-repository/assets/144366612/862da9c1-a94d-4c02-b344-f69ed54cd1d6)
