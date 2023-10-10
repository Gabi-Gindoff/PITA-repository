# Team Report & Updates
  - ### Last Week’s Goals:
      -  The backend worked on developing a webscraper to get all the messages on the IT helpDesk teams channel. Gabi was able to successfully install everything needed to webscrape the teams channel but ran into some issues with possibly needing to login to view the channel. Researched and learning how to use beautifulsoup4 and selenium to scrape the teams webpage. Now we are stuck on how to properly get the messages if a login is needed and errors with the current method. As for the frontend, we are still waiting on the machines to go online. Until then, we are researching how to properly integrate the bot into a customizable website.
  - ### This Week's Progress & Issues:
      - Backend team continued working on the webscraper. Gabi was able to get it to login to the teams chat and scrape the last few messages. Problem with having it automatically scroll to get more than the last eight messages. Been doing some research and it has to do with the way teams is loaded on the webpage. As of right now, you have to scroll and stop at every message but this takes a while and is not a good way of getting all messages. Going to work on another way to see if we can load the data  a different way into the messages list. ------------------FRONTEND UPDATES--------------------
  - ### Next Week’s Plan:
      -  The plan for the backend team is to finish with the webscraper so we can start getting the data into the database. This includes organizing the data, importing it into the database, and making sure all data is correct and looks good. Once that is done we can work on connecting the database to the chatbot.  ------------------FRONTEND UPDATES--------------------

# Contributions of individual team members
  - ### Gabriella:
      - Last Week’s Goals:
          -  Last week I started on the webscraper. I began with all the installations, visual studio, python, pip. Had a problem with accesssing pip but was able to figure it out so now it works. Then I tried using beautifulsoup4 and requests to scrape the teams channel but it wasn't working. Did some research and realized I may need to pivot as the way the messages load on the webpage would not work with the way beautifulsoup was accessing it. So I switched to selenium, did more installations for selenium and chromedriver. Got it to work up to the point where it opens the teams url but think it gets stuck there because you need to login or open it with the teams app. Getting a couple errors. Having trouble figuring out how to get it to properly scrape the teams chat when it needs login info.
      - This Week's Progress & Issues:
          -  This week I was able to get it to properly open the teams channel by loging in with my penn state credentials and read the last couple messages. Still having trouble with getting all the data off the channel but for now at least it is scraping the correct information. I installed the selenium-wire package due to the complexity of handling dynamic content in microsoft teams. I also worked on the software architecture assignment, where we determined the software architecture, software design and coding guidlines for our project.
      - Next Week’s Plan:
          -  The plan for next week is to continue working on the webscraper and hopefully finish it. Once all the data is collected and put into a file, figure out how to get that data into the database. Figure out how to organize and format the data in the database. Once data is in, we have to figure out how to connect the chatbot to the database.
  
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
          - 
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
