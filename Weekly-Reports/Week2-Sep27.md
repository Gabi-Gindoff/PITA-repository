# Team Report & Updates
  - ### Last Week’s Goals:
      - Last week the frontend engineer's started the initial installs for Llama and all of the required Python files. Downloaded Visual Studio code and installed the proper files worked for the initial download of Llama. Learned how to use the command line as well as many different commands to fetch and download files. I had trouble creating a virtual environment and downloading Ubuntu to run a script file. I also had problems downloading the necessary modules for Python. I am currently stuck on running the llama 2 chatbot, many different Python modules are needed, such as pytorch. As of now, all of the current progress is on Adam's laptop. The backend engineer's installed MySql and began by creating a database called `IT_Department`. As of right now the database is being hosted locally on Gabriella's laptop but we may change this later on. We learned how to successfully create a database using the MySql command line. We researched ways to get data from a teams chat into a database but had trouble finding a method that doesn't require direct access to the teams channel. We are stuck on how to retrieve the data/ get the nessaccary permissions and access to the HelpDesk channel. Some team members had trouble installing MySql. 
  - ### This Week's Progress & Issues:
      -  For the backend, had a problem accessing the database that I created in MySql using the command line cause the same port was being used by another application so I created a new database using XXAMP and PhpMyAdmin. IT department is working to see if there is a way for them to give us a file with all the messages from the teams HelpDesk channel but are saying even they don't have the proper access for that. Started researching how to write our own webscrapper to use to get the messages off of teams and began some of the installations needed for this. As for the frontend, Adam was able to install all the proper llama 2 files correctly, but was unable to run the chatbot due to a lack of memory in the GPU. The same issue occurred for both the CPU and GPU versions of the bot. The first problem of pytorch and its corresponding virtual environment issues were solved with some other pip installations, but in the end I could not get the bot to run. I am currently waiting for the powerful school machines to go online so I can download the bot there. 
  - ### Next Week’s Plan:
      -  Plan for the backend is to finish up installations such as pip and other packages/ libraries that will be used for the webscraper and see if we can get it to scrape the messages in a given teams channel. Once this is done we will figure out how to import the data into our database. As soon as the machines go online, the goal for the frontend team is to install and run the chatbot successfully. Once this is achieved, the next step is to integrate the chatbot into its own website. 

# Contributions of individual team members
  - ### Gabriella:
      - Last Week’s Goals:
          - Last week I downloaded MySql on my laptop and created a database that I am currently hosting locally on my computer. I learned about the Microsoft Graph API and thought about trying to use it to get the data from the teams channel but we don't have proper access for it to work. Having trouble determining the best route to get the data into the database that I created. Also learned markdown in order to create the weekly reports in GitHub.
      - This Week's Progress & Issues:
          -  I spoke with multiple staff from the IT department to ask about getting permissions to export one of the teams channels into a file to put in our database. They are working on seeing if they can copy all the data into a file to send to me but at the same time I'm going to start working on writing a webscraper to get the information off the teams channel. I had a problem with the port that the current database in MySql was using so I learned how to use XXAMP and created a new database using that and PhpMyAdmin and will work on importing the data once we have proper access. Briefly tried to use Microsoft Graph API but got stuck when creating the application on Azure cause I didn't have the right permissions. Finished the GitHub setup assignment and updated the README. Successfully created a new database but struggled with pip and python installation to install a package in visual studio. 
      - Next Week’s Plan:
          -  Work on the webscraper for teams and go back to the IT department and see if they have any updates. I began installing pip and python on my laptop but was having trouble so I'm going to continue working on that next week. Decide on what tables we should make and how to format the database so that it is organized and easy to update and find information. 
  
  - ### Adam:
      - Last Week’s Goals:
          -  Understanding and finding proper guides to set up and download the llama 2 chatbot. Mostly researched Llama and other chatbot resources.
      - This Week's Progress & Issues:
          -  Waiting for the machines to go up to install and run the chatbot with the proper hardware. I was able to install the chatbot on my laptop but ran into a memory issue with my GPU preventing me from running the program.
      - Next Week’s Plan:
          -  Once machines are up and running, I will install and run the chatbot. The next step would to be to integrate the bot into its own, public website to be accessed from anywhere.
        
  - ### Treasure:
      - Last Week’s Goals:
          -  ________________________________________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
          
  - ### Harkaren:
      - Last Week’s Goals:
          -  ________________________________________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
        
  - ### Elizabeth:
      - Last Week’s Goals:
          -  Last week I had an issue with installing MySQL server in my personal machine. So after taking to Professor Nate, he suggested to use Redis and installed Redis. 
      - This Week's Progress & Issues:
          -  
      - Next Week’s Plan:
          -  ________________________________________________________________
        
  - ### Katherine:
      - Last Week’s Goals:
          -  ________________________________________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
