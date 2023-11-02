# Team Report & Updates
  - ### Last Week’s Goals:
      - Gabi was able to manually go through the teams channel to pull relevant information to be stored in the database. At first I created the it_department database in MySql Server on my computer but we recreated the same database on Adam's laptop while he was connected to the workstation because we need it to be hosted on the workstation in order for everyone to be able to access it without Gabi opening a port for them on her laptop. After that Gabi and Adam worked together to try to connect the chatbot to the database but we not able to get it to work. We think the problem has to do with the server not currently being hosted properly on the workstation. Treasure created a website with the basic info for the chatbot.
  - ### This Week's Progress & Issues:
      - This week Adam and Gabi worked on setting up a flask connection to our database. After multiple failed attempts, we finally got it set up with a sqlite database with the helpDeskTickets and a flask app which is used for testing right now. We also worked on creating and running pytests. We were able to check these tests visually using the flask app to ensure we can read, insert, and delete from the database. We also worked on creating a yaml file for our CI assignment. Everything builds except running the flask app. We tried adding a script to close the flask app once it opens successfully but it did not work. Going to continue working on this to try to get it all to pass successfully.

  - ### Next Week’s Plan:
      - Next week we hope to connect the chatbot to the database and integrate the chatbot onto the website that Treasure made. Right now the chatbot takes seven minutes to return an answer so Adam is looking into running a smaller model. Our goal is to have a minimal viable product by next week. Researching fastAPI and postman to see which to use.


# Contributions of individual team members
  - ### Gabriella:
      - Last Week’s Goals:
          - Last week I copied in all helpdesk questions and responses from this semester that would be useful for the chatbot to have access to. I created an excel sheet to store the data we wanted to include in our database and then used mySql to add the data into the database on MySql server. I realized that I don't want to open a port on my computer to give everyone access to my laptop as it opens my computer to risks of being hacked through the open portal. Going to try to connect to the workstation to host the database there and just recreate it using the script I created.
      - This Week's Progress & Issues:
          - This week I worked on setting up our database with Flask. I followed tutorials about setting up the connection (askpython) and watched lectures/videos on cs50 flask (harvard) recommended by Professor Wagenhoffer. First I tired connecting flask with the database that was hosted on my laptop on mysql server. Then I tried setting it up with XXAMP and PhpMyAdmin but there was a problem with the connection. With the professor's help, I was able to set up the connection between a sqlite database with flask using our repo's codespace. I also worked with Adam to add and run pytests, and then set up our CI using GitHub Actions.

      - Next Week’s Plan:
          - Next week my goal is to work on connecting the flask application and sqlite database with the chatbot. Once that is done, we can work on integrating the chatbot onto the website that Treasure has been developing and designing. If we have time, I can manually add more data from the teams channel into our database.

  
  - ### Adam:
      - Last Week’s Goals:
          - I tried to host a local database server on my laptop, but was unsuccessful in doing so due to the chatbot not being able to connect to the port. We have tried multiple solutions but found out that it is a problem with the workstations blocking ports.
      - This Week's Progress & Issues:
          - Gabi and I got a sqlite server up and running through flask and github codespaces. We also got CI up and running with a successful build
      - Next Week’s Plan:
          - The plan is to finally connect the local database to the chatbot and be able to read from it.
        
  - ### Treasure:
      - Last Week’s Goals:
          - I created a website for the chatbot and used github pages to create a public link to access the website. I am currently working on making the chatbot interface so that it can be interactive with the user's inputs. Using HTML, CSS, and some javascript with ajax.
      - This Week's Progress & Issues:
          - The frontend members modified the website to run using flask. The website allows for users to interact and type into the chatbot form, while also taking in and storin user inputs.
      - Next Week’s Plan:
          - The goal for next week is to be able to figure out how to integrate the chatbot, local hosted, onto an actual url website since github pages is not working well anymore.

          
  - ### Harkaren:
      - Last Week’s Goals:
          - We currently have a basic website for the chatbot to be integrated to. We will be making modifications to the website as needed. I will begin to start researching how to integrate the chatbot into the website by watching some youtube videos. Hopefully since the machines are running we will be able to connect the database, chatbot and website together.
      - This Week's Progress & Issues:
          - With the goal from last week being the machines running we should be able to have the website, database and chatbot working together. But the frontend members modified the previous website to the one that is using flask. 
      - Next Week’s Plan:
          - The goal for next week is for the front end to evaluate if this should be locally hosted onto an actual website (url) and integrate the chatbot.  
        
  - ### Elizabeth:
      - Last Week’s Goals:
          - Last week filtering questions and answers from IT team's chat not done completely still working on it. 
      - This Week's Progress & Issues:
          - This week we are working on Testing and CI assignment. 
      - Next Week’s Plan:
          - Hopefully by next week I will start connecting to the database and start coding 
        
  - ### Katherine:
      - Last Week’s Goals:
          - Imported data from the excel spreadsheet into the database. 
      - This Week's Progress & Issues:
          - Tested within the database to make sure basic queries worked. Then made test cases using pytest, I don’t think these test cases were used though. 
      - Next Week’s Plan:
          - I think we still need to get the database connected to the chatbot. 
