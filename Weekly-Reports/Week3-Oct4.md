# Team Report & Updates
  - ### Last Week’s Goals:
      -  For the backend, had a problem accessing the database that I created in MySql using the command line cause the same port was being used by another application so I created a new database using XXAMP and PhpMyAdmin. IT department is working to see if there is a way for them to give us a file with all the messages from the teams HelpDesk channel but are saying even they don't have the proper access for that. Started researching how to write our own webscrapper to use to get the messages off of teams and began some of the installations needed for this. As for the frontend, Adam was able to install all the proper llama 2 files correctly, but was unable to run the chatbot due to a lack of memory in the GPU. The same issue occurred for both the CPU and GPU versions of the bot. The first problem of pytorch and its corresponding virtual environment issues were solved with some other pip installations, but in the end I could not get the bot to run. I am currently waiting for the powerful school machines to go online so I can download the bot there.
  - ### This Week's Progress & Issues:
      -  The backend is working on developing a webscraper to get all the messages on the IT helpDesk teams channel. Gabi was able to successfully install everything needed to webscrape the teams channel but ran into some issues with possibly needing to login to view the channel. Researched and learning how to use beautifulsoup4 and selenium to scrape the teams webpage. Now we are stuck on how to properly get the messages if a login is needed and errors with the current method. As for the frontend, we are still waiting on the machines to go online. Until then, we are researching how to properly integrate the bot into a customizable website.
  - ### Next Week’s Plan:
      -  The plan for the backend team is to finish up with the webscraper so we can deal with getting the data into the database. This includes organizing the data, importing it into the database, and making sure all data is correct and looks good. Once that is done we can work on connecting the database to the chatbot. For the frontend, we plan on finalizing the integration process of the chatbot and the website and style the site as well. 
# Contributions of individual team members
  - ### Gabriella:
      - Last Week’s Goals:
          -  I spoke with multiple staff from the IT department to ask about getting permissions to export one of the teams channels into a file to put in our database. They are working on seeing if they can copy all the data into a file to send to me but at the same time I'm going to start working on writing a webscraper to get the information off the teams channel. I had a problem with the port that the current database in MySql was using so I learned how to use XXAMP and created a new database using that and PhpMyAdmin and will work on importing the data once we have proper access. Briefly tried to use Microsoft Graph API but got stuck when creating the application on Azure cause I didn't have the right permissions. Finished the GitHub setup assignment and updated the README. Successfully created a new database but struggled with pip and python installation to install a package in visual studio.
      - This Week's Progress & Issues:
          -  This week I started on the webscraper. I began with all the installations, visual studio, python, pip. Had a problem with accesssing pip but was able to figure it out so now it works. Then I tried using beautifulsoup4 and requests to scrape the teams channel but it wasn't working. Did some research and realized I may need to pivot as the way the messages load on the webpage would not work with the way beautifulsoup was accessing it. So I switched to selenium, did more installations for selenium and chromedriver. Got it to work up to the point where it opens the teams url but think it gets stuck there because you need to login or open it with the teams app. Getting a couple errors. Having trouble figuring out how to get it to properly scrape the teams chat when it needs login info. 
      - Next Week’s Plan:
          -  Continue working on the webscraper and hopefully finish it (going to ask professor Wagenhoffer for help). Once all messages are put into a file, figure out how to get that data into the database either using phpMyAdmin or MySql server. Figure out how to organize and format the data in the database. Once data is in, we have to figure out how to connect the chatbot to the database.
  
  - ### Adam:
      - Last Week’s Goals:
          -  Waiting for the machines to go up to install and run the chatbot with the proper hardware. I was able to install the chatbot on my laptop but ran into a memory issue with my GPU preventing me from running the program.
      - This Week's Progress & Issues:
          -  Still waiting on the machines to go up, as soon as they do, I will begin the process of running the chatbot on them. I will then begin to integrate the bot into its own, public website.
      - Next Week’s Plan:
          -  Clean up all of the issues of the integration process and properly log the download and integration process for future use.
        
  - ### Treasure:
      - Last Week’s Goals:
          -  Researched ways to integrate the Llama chatbot into a website. Preparing in advance for when we are able to have the chatbot up and running.
      - This Week's Progress & Issues:
          -  The chatbot is now running and is in the process of being used through the provided machines.
      - Next Week’s Plan:
          - By next week, we hope to have a plan on how to integrate the chatbot into a website free of cost. Being able to use it through its own web-interface freely.
          
  - ### Harkaren:
      - Last Week’s Goals:
          -  Gaining more knowledge on llama. Brainstorming on making a website thats needed using flask or django. Found some videos that I will watch to begin creating a map on where to begin.
      - This Week's Progress & Issues:
          -  Was able to find a good starting for the website. There was a couple of youtube videos that I thought will be of great use (will share with frontend in class), still waiting on chatbot to run on machines. Maybe finally being able to pick which what we would like to use whether its django/flask with Python or typescript and react.
      - Next Week’s Plan:
          -  Hopefully the machines will begin to work by this week with the chatbot so we can begin to set up the website. Also meet iwth other front end members to decide on on which we will use to create the website. 
  - ### Elizabeth:
      - Last Week’s Goals:
          -  ________________________________________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
        
  - ### Katherine:
      - Last Week’s Goals:
          -  Created a basic ER Diagram with tables and fields I think we'll need, relationships, and thought about potential queries.
      - This Week's Progress & Issues:
          -  This week I started on the database, used the ER Diagram to help create tables and included fields. I used MySQL workbench. I created the Account table for the user and included PSU ID as the primary key, but wondering if it's better to just do email because no one remembers their PSU ID. 
      - Next Week’s Plan:
          -  Hopefully work on putting the data into the database. I'm thinking if we sort the data by categories, we can include a category field in the Information table, and the chatbox can ask the user what category their question would be in to help narrow it down. Then create a query that selects information from the category.
