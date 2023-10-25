# Team Report & Updates
  - ### Last Week’s Goals:
      -  For the backend, Gabi tried finishing the webscraper but bumped into another problem with how Microsoft teams is loaded when loading it on a webpage. Wagenhoffer said we can scrap it and start manually adding data from the teams channel. Started going through to get relevant information in order to create proper tables for the database. For the frontend, we have finally been able to run llama 2 on the school machines. The goal of this week is making everyone understand how to connect to the machines and run it on their devices. After that, we will continue to work on designing the website.
  - ### This Week's Progress & Issues:
      -  Gabi was able to manually go through the teams channel to pull relevant information to be stored in the database. At first I created the `it_department` database in MySql Server on my computer but we recreated the same database on Adam's laptop while he was connected to the workstation because we need it to be hosted on the workstation in order for everyone to be able to access it without Gabi opening a port for them on her laptop. After that Gabi and Adam worked together to try to connect the chatbot to the database but we not able to get it to work. We think the problem has to do with the server not currently being hosted properly on the workstation. Treasure created a website with the basic info for the chatbot. 
  - ### Next Week’s Plan:
      -  Ensure the database is being hosted properly on the workstation and then connect the chatbot to the database. Make sure the chatbot can grab information from the database. Then we need to integrate the chatbot onto the website and get it fully working to the point where a user can enter in a question and an answer will be displayed.

# Contributions of individual team members
  - ### Gabriella:
      - Last Week’s Goals:
          -  Last week I continued with the webscraper until I was having a problem with loading more than 10 messaged. I realized that it was because it is loaded dynamically and there is no way for it to automatically scroll to load more messages. After lots of googling and trying out various solutions, nothing seemed to work. Spoke to the professor and decided to start manually going through the teams channel and copying over the information we need for the chatbot. Decided on tables to include in the database that correspond to the categories of possible questions that the IT student workers encounter. 
      - This Week's Progress & Issues:
          -  This week I copied in all helpdesk questions and responses from this semester that would be useful for the chatbot to have access to. I created an excel sheet to store the data we wanted to include in our database and then used mySql to add the data into the database on MySql server. I realized that I don't want to open a port on my computer to give everyone access to my laptop as it opens my computer to risks of being hacked through the open portal. Going to try to connect to the workstation to host the database there and just recreate it using the script I created. 
      - Next Week’s Plan:
          -  My plan for next week is to get the databaase hosted on the workstation and then to connect the database to the chatbot so we can begin testing. If we have more time, I can add more data to the database but I want to focus on getting the basics working before adding more. 
  
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
          - This week we are trying to still make the machines run but have started to work on the website. I provided the text in regards to the chat bot that explained what it will do and the contact for the IT department that will be implemented into the website.
      - This Week's Progress & Issues:
          -  We currently have a basic website for the chatbot to be integrated to. Maybe will make modifications as needed. I will begin to start researching how to integrate the chatbot into the website by watching some youtube videos. Hopeully the machines will be running on each of our devices by then.  
      - Next Week’s Plan:
          -  Since the machines are running we should be able to have the website, database and chatbot working together by this week. 
  - ### Elizabeth:
      - Last Week’s Goals:
          - Met with Gabi and Katherine to talk about the project and decided to go through IT teams chat and find the most common questions and answers and put that in the excel spreadsheet.  
      - This Week's Progress & Issues:
          -  This week continue with the 
      - Next Week’s Plan:
          -  ________________________________________________________________
        
  - ### Katherine:
      - Last Week’s Goals:
          -  I modified the database, added a category field to the Information table.
      - This Week's Progress & Issues:
          -  Recieved the data from Gabi in an excel spreadsheet. For some reason, it wouldn't import the data when I used MySQL workbench, so I copied it over to PHPAdmin, imported the data and that worked. I just need to upload it to the github.
      - Next Week’s Plan:
          -  Start working on getting the database connected to the chatbot.
