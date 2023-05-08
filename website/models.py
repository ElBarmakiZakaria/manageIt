#from sqlalchemy import func #for date
from flask_login import UserMixin
from . import db, cursor




class Tasks():
   # cursor.execute("DROP TABLE IF EXISTS yourtablename")


    cursor.execute("""CREATE TABLE IF NOT EXISTS Tasks 
                   (TaskId INT AUTO_INCREMENT PRIMARY KEY, 
                   User_email VARCHAR(100),
                   FOREIGN KEY(User_email) REFERENCES Users(email), 
                   Task_title VARCHAR(100), 
                   Task_description VARCHAR(100),
                   Task_priority VARCHAR(10),
                   Task_status VARCHAR(10),
                   Task_date VARCHAR(50))""")

    


    def add_task(self, User_email, Task_title, Task_description, Task_priority, Task_status, Task_date):
        cursor.execute("INSERT INTO Tasks (User_email, Task_title, Task_description, Task_priority, Task_status, Task_date) VALUES (%s, %s, %s, %s, %s, %s)",
                        (User_email, Task_title, Task_description, Task_priority, Task_status, Task_date))
        db.commit()


    def update_task(self, id, Task_title, Task_description, Task_priority, Task_status, Task_date):
        cursor.execute("""
        UPDATE Tasks
        SET     Task_title = %s,
                Task_description = %s,
                Task_priority = %s,
                Task_status = %s,
                Task_date = %s
        WHERE TaskId = %s
        """, (Task_title, Task_description, Task_priority, Task_status, Task_date, id))
        db.commit()
        cursor.execute("SELECT * FROM Tasks")
        for s in cursor:
            print(s)
        print(Task_title, Task_description, Task_priority, Task_status, Task_date, id)


    def delete_task(self, id):
        cursor.execute("DELETE FROM Tasks WHERE TaskId = %s", (id,))
        db.commit()



class User(UserMixin):

    cursor.execute("""CREATE TABLE IF NOT EXISTS Users 
    (userID INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(40), email VARCHAR(100), password VARCHAR(100))""")
    
    # cursor.execute("SELECT * FROM Users")
    # for x in cursor:
    #     print(x)
    

    

    
    def __init__(self, id=None, username=None, email=None, password=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def add_user(self, Username, Email, Password):
        print("here done1")
        cursor.execute("INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)", (Username, Email, Password))
        db.commit()
        print("here done2")
        # cursor.execute("SELECT * FROM Users")
        # for x in cursor:
        #     print(x)

    def check_logging(self, Email):
        try:
            cursor.execute("SELECT * FROM Users WHERE email =  %s ", (Email,))
            user = cursor.fetchall()

            return user
        
        except IndexError:
            return None
        
    def load_user(self, id):
        try:
            cursor.execute("SELECT * FROM Users WHERE userID = %s", (id,))
            user = cursor.fetchall()

            return User(user[0][0], user[0][1], user[0][2], user[0][3])
        except IndexError:
            return None
    
    

    
