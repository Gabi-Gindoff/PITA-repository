import mysql.connector


#TO DO 
#REPLACE USERNAME, PASSWORD AND DATABASE NAME WITH ORIGINAL CREATOR 

cnx = mysql.connector.connect(user='username', password='password',
                              host='127.0.0.1',
                              database='it_department')
cnx.close()
