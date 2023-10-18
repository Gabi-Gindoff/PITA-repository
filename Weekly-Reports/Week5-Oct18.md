# Team Report & Updates
  - ### Last Week’s Goals:
      -  Backend team continued working on the webscraper. Gabi was able to get it to login to the teams chat and scrape the last few messages. Problem with having it automatically scroll to get more than the last eight messages. Been doing some research and it has to do with the way teams is loaded on the webpage. As of right now, you have to scroll and stop at every message but this takes a while and is not a good way of getting all messages. Going to work on another way to see if we can load the data a different way into the messages list. For the frontend, we are still waiting on the machines to go online. Until then, we are still looking into how to properly integrate the bot into a customizable website. We have found some good resources for the website's design and to integrate everything into it.
  - ### This Week's Progress & Issues:
      -  For the backend, Gabi tried finishing the webscraper but bumped into another problem with how microsoft teams is loaded when loading it on a webpage. Wagenhoffer said we can scrap it and start manually adding data from the teams channel. Started going through to get relevant information in order to create proper tables for the database. -----------------------------FRONTEND-----------------------------
  - ### Next Week’s Plan:
      -  As for the backeng, continue going through as much of the teams channel as we can to get as many helpdesk messages as possible. Goal is to create at least one or two tables with enough information so that the following week we can connect it to the frontend and start testing.  -----------------------------FRONTEND-----------------------------

# Contributions of individual team members
  - ### Gabriella:
      - Last Week’s Goals:
          -  Last week I was able to get it to properly open the teams channel by logging in with my penn state credentials and read the last couple messages. Still having trouble with getting all the data off the channel but for now at least it is scraping the correct information. I installed the selenium-wire package due to the complexity of handling dynamic content in microsoft teams. I also worked on the software architecture assignment, where we determined the software architecture, software design and coding guidlines for our project.
      - This Week's Progress & Issues:
          -  This week I continued with the webscraper until I was having a problem with loading more than 10 messaged. I realized that it was because it is loaded dynamically and there is no way for it to automatically scroll to load more messages. After lots of googling and trying out various solutions, nothing seemed to work. Spoke to the professor and decided to start manually going through the teams channel and copying over the information we need for the chatbot. Decided on tables to include in the database that correspond to the categories of possible questions that the IT student workers encounter. 
      - Next Week’s Plan:
          -  Next week my plan is to continue manually going through the IT department's teams channel and write it all down either in an excel sheet that we can upload into the database or write SQL commands to add it straight into the database. 
  
  - ### Adam:
      - Last Week’s Goals:
          -  ________________________________________________________________
      - This Week's Progress & Issues:
          -  ________________________________________________________________
      - Next Week’s Plan:
          -  ________________________________________________________________
        
  - ### Treasure:
      - Last Week’s Goals:
          -  Began researching free solutions and met via zoom on how to integrate it and host it into a website without the need to spend money now that the chatbot are going to be able to run on the machines provided.
      - This Week's Progress & Issues:
          -  Currently in the process of creating the website that the chatbot will be hosted on.
      - Next Week’s Plan:
          -  Hopefully we can find a solution on how to integrate the chatbot onto a seperate website.
          
  - ### Harkaren:
      - Last Week’s Goals:
          - This week we are still waiting on the machines to be running. We are attempting to find a free platform to use for the websites. We met over zoom and discussed briefly about the website with other front end members to decide on where we will begin to outline a bit of the website.
     
      - This Week's Progress & Issues:
          -  This week we are trying to still make the machines run but have started to work on the website. I provided the text in regards to the chat bot that explained what it will do and the contact for the IT department that will be implemented into the website.    
      
      - Next Week’s Plan:
          -  Hopefully this week the machines will be up running and the website will be done. 
        
  - ### Elizabeth:
      - Last Week’s Goals:
          -  This week we worked on the software architecture assignment and talked to the group regarding project scheduling,                    coding gidlines etc.
      - This Week's Progress & Issues:
          -  Planning to start adding data to databases. Also start learning SQL into more depth and start working on the codings.
      - Next Week’s Plan:
          -  Next week start looking through IT team messages to see what are the common issues that IT department faced in the past
        
  - ### Katherine:
      - Last Week’s Goals:
          -  looked into react 
      - This Week's Progress & Issues:
          -  Met with Gabi and Elizabeth. Sounds like we're going to manually get about a year's worth of data from the microsoft teams chat, enter the questions, answers, and related category into excel. Then we're going to upload that into the database. Going to add the category field in the Information table. So going to start getting the data from the chat and putting it into excel.
      - Next Week’s Plan:
          -  Planning to continue getting data from the microsoft teams chat into excel
