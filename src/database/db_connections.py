import mysql.connector
from mysql.connector import Error

# =========================
# Database Configuration
# =========================
DB_CONFIG = {
    "host": "172.29.32.1",   # Your Windows MySQL host IP for WSL
    "user": "expense_user",
    "password": "Mysql@2380",
    "database": "personal_expense",
    "port": 3306,
    "connection_timeout": 5
}


def connect_db():
    """
    Establish and return MySQL database connection.
    Returns:
        connection object if successful
        None if connection fails
    """
    try:
        print("Trying to connect to MySQL...")

        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            print("Connected to MySQL successfully!")
            return connection
        else:
            print("MySQL connection failed.")
            return None

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def close_db(connection):
    """
    Safely close the MySQL database connection.
    """
    try:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")
    except Error as e:
        print(f"Error while closing MySQL connection: {e}")