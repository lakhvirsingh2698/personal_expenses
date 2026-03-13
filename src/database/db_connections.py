import mysql.connector
from mysql.connector import Error

def connect_db():
    """connect to mysql database and return back"""

    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Mysql@2380",
            database = "personal_expense"
        )
        if connection.is_connected():
            print("connected to Mysql databse")
            return connection
        
    except Error as e:
        print(f"Error connecting to mysql: {e}")
        return None
    
def close_db():
    """close Mysql databse"""
    if connection and connected.is_connected():
        connection.close
        print("Mysql Connection closed")
        