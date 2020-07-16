import mysql.connector
address = 'localhost'
username = 'root'
password = '42534253'
db = 'streamer'
class ConnectToDB():
    
    def connect(self):
        mydb = mysql.connector.connect(
            host = address,
            user = username,
            passwd = password,
            database = db
        )
        return mydb