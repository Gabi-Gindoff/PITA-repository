import sqlite3

# Connect to the database
conn = sqlite3.connect('it_Department')
cursor = conn.cursor()

# Insert data into the table
#cursor.execute("INSERT INTO my_table (name, age) VALUES (?, ?)", ('John', 25))
#cursor.execute("INSERT INTO my_table (name, age) VALUES (?, ?)", ('Jane', 30))


cursor.execute ('''INSERT INTO HelpDeskTickets (infoID, question, response, responseDate, category) VALUES
                 (1, 
                 'can someone at TSC check room 10 downstairs in the library and see what the issue with the computer is? We will most likely open a ticket if you can''t revive it but we need to a little more info first .the monitor keeps entering power saver mode, even though the computer is plugged in and on. The screen said that it''s not receiving a signal from the computer. Is there a way to fix this?',
                  'I will put that in the ticket.', 
                  '2023-10-12', 
                  'Monitor')''')


cursor.execute('''
    INSERT INTO HelpDeskTickets (infoID, question, response, responseDate, category)
    VALUES
        (3, 'Room 216 need to turn on the another projector number 2 but it’s not Turning on', 'Check the mode its in, it might need to be in collaboration/ interactive mode. Also you can try turning them on manually on the actual projector. Try a restart of the system', '2023-10-13', 'Projector'),
        (4, 'Do we have any of those usb to headphone Jack adapters in Sutherland or woodland?', 'We do have some in Woodland. I can''t remember if there were any in 218 in those plastic drawers', '2023-10-13', 'Cables'),
       (5, 'A student is trying to download IBM SPSS Statistics on their computer, but it is not downloading.', 'Try fixing with updates and Wi-Fi connection', '2023-10-16', 'Software'),
       (6, 'is there a way to print smaller. A student has notes on Google docs he wants to glue onto a notecard.', 'He''d have to switch it in the doc i believe', '2023-10-16', 'Printer'),
       (7, 'we have a student here (abf5704) who cant send or receive emails, any ideas as to why that might be?', 'use the actual outlook app', '2023-10-16', 'Software'),
       (8, 'library room 5 display isn’t coming?', 'power cable end was pulled out due to lack of slack in the box, velcro to the desk now for fewer moving parts', '2023-10-17', 'Display'),
       (9, 'This printer in CLAW hasn’t been working since last semester, and it gives two contradictory warnings that say the paper tray is both overfilled and empty. Is there a way to fix this or should I just tell CLAW that perhaps they should order a new printer?', 'No. Have the responsible party put in a ticket, please, so someone can take a look. Ticket = email to abit@psu.edu', '2023-10-17', 'Printer'),
       (10, 'Please head down to S215 and see if you can help the teacher. issue where her MS Word isn''t displaying images at certain times', 'Dr. Harvell is going to send in a ticket.', '2023-10-17', 'Software')
'''
)

cursor.execute('''
   INSERT INTO HelpDeskTickets (infoID, question, response, responseDate, category)
   VALUES
       (11, '218 - please go check the print kiosk upstairs in Sutherland and make sure it does not have any error message.', 'Just checked, it''s all good', '2023-10-18', 'Printer'),
       (12, 'Can somebody check if there was a ticket submitted for the library room 10. The professor is Katie Odhner. She wants to be kept in the loop about the progress.', 'That ticket has been submitted and someone will probably follow up tomorrow. Let her know that she is included on the ticket, so updates will probably come by email.', '2023-10-18', 'Ticket'),
       (13, 'room w222 need help she is trying to open a video and the sound is not working. How do I fix that ?', 'Change the sound settings on the pc to crestron if its an option in the sound settings', '2023-09-26', 'Sound'),
       (14, 'Please check on S306. Reported a dim display on podium- could be a simple brightness control on the menu', 'get the service number from the back of the monitor. most likely its a failed display. Anthony needs the number for a dell service call', '2023-09-26', 'Display'),
       (15, 'Can you come to s208 to help with the room cameras? Or give us an idea of what the issue could be', 'Try checking the mode', '2023-09-25', 'Camera'),
       (16, 'room 10 in the library ground floor woodland Tower not outputting display to projector, projector on, got monitor to work eventually', 'Restart monitor and projector', '2023-09-25', 'Display'),
       (17, 'could someone head over to Springhouse 100 and help the professor get the projector powered on? Not turning on. There''s a flashing red light and a solid red', 'Check the input on the tv remember we had to play with it a little for it to show up on screen. I was able to revive it by unplugging , giving it some time and replugging but the lamp will go soon so we should replace when we get the chance', '2023-09-25', 'Projector'),
       (19, 'could some run over to Sutherland 213 and help the professor with sound? Reporting static type sounds through the speakers', 'Troubleshoot in settings under sound', '2023-09-25', 'Sound'),
       (20, 'I''m at the Hispanic event and their an application not playing on the speaker ?!? The app is record box', 'The sound system works but their equipment doesn''t. We don''t support their gear so there isn''t much we can do except check on the obvious. They were OKAY with being able to play a playlist.', '2023-09-22', 'Software')
'''
)

cursor.execute('''
   INSERT INTO HelpDeskTickets (infoID, question, response, responseDate, category)
   VALUES
       (21, 'mic is not working, not getting on', 'Did you check to make sure the batteries are fresh and inserted correctly. Try pressing the power button a little longer', '2023-09-21', 'Mics'),
       (23, 'I need you to stop in W340 at 9 AM and get the class up and running for a zoom hybrid. Gilya is out today and sent a link in canvas to the students.', 'You will need to have one of the students login to the podium PC and set it up that way.', '2023-09-21', 'Zoom Setup'),
       (24, 'does anyone know how a student can turn something from the python software to a .py file?', 'Pretty vague question. But overall, you will create a .py file using an IDE like PyCharm, Notepad, etc. The .py extension indicates to the system that it is a Python file and it needs to run with the Python interpreter to read, understand, and execute the instructions in the .py file', '2023-09-20', 'Software'),
       (25, 'have a student who got a MacBook from the library, and they cannot log in. Apparently, someone who loaned it before put a password on it. Any ideas', 'I got it to log in by doing a hard reset on it.', '2023-09-20', 'Computer'),
       (26, "cant get the cam working in 317A, just a black screen. Any ideas", "if the Instalink software is open, you have to click the allow other software to control or close that software. You can also try tapping the flat spot of the camera where the Instal logo is twice to recenter the cam", '2023-09-20', 'Camera'),
       (27, "can someone confirm if the setup is completed for an event by CPD at Sutherland Plaza?", 'you will need to take down the sound system and red bag with a wireless mic and a MacBook', '2023-09-20', 'Event Setup'),
       (28, 'we have a student trying to get an IBM program from software.psu, and it says the license is expired. Any ideas?', "Did they get a license info from software.psu.edu checkout process and attempt to apply the license? If so, and they are getting an error message, contact the software.psu.edu folks and explain the situation. They may have to look into it or generate a new license for the user if applicable. I believe the contact info for the site should be on the page somewhere. The user has to email them. Have the student email psulss@psu.edu", '2023-09-19', 'Software'),
       (29, 'a student wants to know if they can use their own paper in one of the printers in Woodland. Who would I even direct them to for an answer?', 'the WEPA printers are self-contained, and you cannot use your own paper in them', '2023-09-19', 'Printer'),
       (30, "there is a professor in 211. He wants all the projectors to show his screen, but only one is. Do you know how to get the other 6 working?", "Make sure to go to the main menu and ensure Collaborative mode is selected. Then select the professors computer (laptop or podium) on the left and the All button on the right (will need to give it time to warm up)", '2023-09-18', 'Projector'),
       (31, 'please check the printer in the lobby again, we have a report that it is frozen and not responding. Let me know if you can print something from there or not.', "It was stuck on the login screen, but I used my phone to login, and it fixed it", '2023-09-18', 'Printer'),
       (32, 'Can someone help in S227 to get the podium and projector up and running?', "we just added two screens in that room. The front projector will work, and the two NEC on the sides using the remote. Had to go into settings and set the display options to duplicate this screen or something like that", '2023-09-15', 'Projector'),
       (33, "Im gonna send over Fengchang Yang, shes having problems with Zoom, and its not detecting her microphone. She also needs proof that she spoke to IT because of her Professor. Shes also having another issue with her email, but Im not too sure what exactly the problem is.", 'Send her to Woodland 347', '2023-09-15', 'Software'),
       (34, 'Someone please run a box of AA batteries to the equipment rack in Lubert Commons', 'batteries in 218', '2023-09-14', 'Batteries'),
       (35, "need someone to head to S309 for a computer assist. Reporting computer isnt displaying", 'check input setting', '2023-09-13', 'Display'),
       (36, 'Need the (4) lockdown Macs brought over to 347 this afternoon.', 'The lockdown Macs are the ones 1-4 in the cart', '2023-09-12', 'Computer Cart'),
       (37, 'A professor forgot their phone and is wondering if she can send the authorization to her work phone so she can log onto canvas?', 'they need to call 814-865-HELP (4357) for a one-time token or to have them adjust 2FA settings like that', '2023-09-11', 'Two Factor Authentication'),
       (38, 'how to see room availability', 'https://25live.collegenet.com/pro/psu#!/home/search/location/calendar', '2023-09-08', 'Resources'),
       (39, "Theres an issue in S206, the sound isnt playing. We tried both speakers and checked the audio mute", "After restarting the Crestron, I turned the volume knob up on the Crestron, and it seemed to work. Why this system has 3 volume knobs is", "2023-09-08", "Sound"),
       (40, 'Student is unable to receive emails from canvas, her email is: CXB5955@psu.edu. It says canvas is unable to send messages to this email', 'can they jump into our Zoom room? https://psu.zoom.us/my/oitvirtualoffice. To close the loop on this, we were unable to get the user notifications to work after removing/re-adding psu email. A ticket with the Canvas team was created so they can provide additional assistance to the user.', '2023-09-08', 'Software')
'''
)


cursor.execute('''
   INSERT INTO HelpDeskTickets (infoID, question, response, responseDate, category)
   VALUES
       (41, 'We have a last minute request to provide speakers and music in the Sutherland plaza. Please start pulling the sound system down to the plaza to setup along with a mac for sound. I will be coming over shortly.', 'sound system in Andys room. The anchor spund sound system. Take that down along with the speaker cable and stands and MacBook', '2023-09-07', 'Event Setup'),
       (42, 'a student is trying to download a presentation on one of the library desktops and gets an error message. Is there a way to fix to download without getting an error?', 'sounds like they have exceeded their quota.All files stored on desktop/gocuments/downloads/pictures combined only have 1gb total space. They would have to delete old files that no longer need to free up space for new stuff', '2023-09-06', 'Software'),
       (43, 'Hes looking for a software and Im unsure if we have it', ' If they are looking for software to be installed on the lab machines they should put in a ticket by emailing "abit@psu.edu". Send up to 347', '2023-09-06', 'Software'),
       (44, 'Can someone stop by S206 and help turn the projector on?', 'n S206 someone keeps turning off the projector manually at the end of the day. Need to flip the switch on the projector', '2023-08-31', 'Projector'),
       (45, 'Trying to login to account but says password is incorrect', 'reset via accounts.psu.edu', '2023-10-21', 'Software'),
       (46, 'need someone to run over to S204 and help mthe professor connect to the projector The professor wants to use both projectors in S204. Is there a way to do that?', 'Yes; hold the button down for about 4-5 seconds and the second projector should come on.', '2023-08-30', 'Projector'),
       (47, 'can someone run down to S305 and check the lav mic and make sure it works in the room and can be heard through the speakers', 'Okay. First thing you can check is to make sure the belt Pac and receiver are on the same frequency and that the batteries are good and that there is no corrosion on the battery contacts. If all that checks out Ill need to bring in the laptop and check the crestron settings', '2023-08-30', 'Equipment'),
       (48, 'W237 the headphones are not working for most of the computer when students plug it to the port', 'Headphone have to be plugged in before you login. If you are currently logged in. Log out. Unplug replug headphone. And log back in', '2023-08-29', 'Sound'),
       (49, 'Need someone to go down to S309 and help with a projection issue. projector is showing no signal. Is there a way to fix that?', 'Do a Crestron reset', '2023-08-29', 'Projector'),
       (50, 'Having trouble in room 204, the display works, the computer will connect to the display, but not the monitor', 'Make sure its not extended mode', '2023-08-29', 'Projector'),
       (51, 'Does the scanner to the right of the computers in the front work, or are students just supposed to use the wepa scanner?', 'Woukd recommend the wepa scanner. You can save directly to OneDrive if you have it linked', '2023-08-25', 'Printer'),
       (52, 'Does anyone know how to connect the portable microphones to zoom? I changed the batteries and the light is on, but none of the options are working', 'The mics use one of the USB options, worse case use the webcam option for your zoom mic. Also check what aux port the cable is plugged into, should be pink. Channel should match the one on the box thats by the pc', '2023-08-24', 'Microphone'),
       (53, 'S206 projector not turning on', 'switch the rocker power switch on projector to on', '2023-08-24', 'Projector'),
       (54, 'does anyone know how to drop the screen for the projector in Sutherland 311?', 'There should be a little switch on the wall by the podium', '2023-08-23', 'Projector'),
       (55, 'Does this new library staff member need to call Upark in order to get into the microsoft 2FA or can we help her with that, its apparently her first time setting it up?', 'If they dont have a backup device to mfa they will have to call up', '2023-08-23', 'Two Factor Authentication'),
       (56, 'is there any extra mouses. The one in claw room is broken', 'have the claw supervisor reach out and we can more ordered', '2023-08-23', 'Equipment'),
       (57, 'there are some students asking for a room to take their zoom classes in. Are there any rooms they can use?', 'Conference center is the official designated room, right past Rydal', '2023-08-22', 'Resources'),
       (58, 'how to see room availability', 'visit https://25live.collegenet.com/pro/psu#!/home/search/location/calendar', '2023-08-21', 'Resources'),
       (59, 'A student is trying to use Microsoft Authenticator to sign into lion path, but the app isnt working. She tried reinstalling it, but the problem persists', 'have them contact the helpdesk at 814-865-4357', '2023-08-21', 'Software'),
       (60, 'A student is having trouble logging into the the connecting to the Wi-Fi. When I try and log into guest, it says an error has occurred', 'I would give it the standard turn wifi on and off, recheck, reboot, recheck.  If that doesnt work, they could be blocked so they need to turn off wifi for atleast an hour, maybe 1hr 30, then give guest another shot', '2023-08-21', 'Wifi'),
       (61, 'instructor needs assist in Woodlsand 132A connecting his laptop', 'hdmi switch set to blueray for projector instead of hdmi.', '2023-08-21', 'Monitor'),
       (62, 'professor just needs help logging into the PC. Only signed in user can unlock error', 'Reboot it. Bottom right corner should allow you to shut down still...worst case hold the power button on the PC to force it off', '2023-08-21', 'Monitor'),
       (63, 'if someone want to borrow the laptop where they have to go ?', 'They should complete this form: https://pennstate.service-now.com/sp?id=sc_cat_item&sys_id=515334ec1b1c1c106d6765302a4bcb33 and then theyll get an email when the device is ready.', '2023-08-21', 'Resources'),
       (64, 'S208 Only projector 1 is showing the lectern pc, the others are just showing what looks like the interactive screen', 'On the touch panel there is a screen that will allow you to manually choose where to send the source. Sometimes you will need to choose the send to all feature', '2023-08-21', 'Projector'),
       (65, 'How to print on Campus?', 'Download WePaw app. Visit https://pawprints.psu.edu/ for step by step instructions', '2023-08-20', 'Printer'),
       (66, 'How to connect to the wifi?', 'Connect the psu wifi with your penn state credentials', '2023-08-20', 'Wifi'),
       (67, 'Where are the IT locations?', 'Sutherland 218, Woodland Library/ TSC, and Woodland 347', '2023-08-20', 'Resources'),
       (68, 'Where are the printers located?', 'Woodland lobby, Woodland 344, Sutherland 3rd floor hallway, the ground floor of Lares, and at Lions Gate', '2023-08-21', 'Printer');
'''
)




# Commit the changes and close the connection
conn.commit()
conn.close()