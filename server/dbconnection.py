import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         database="server_table_rsa"
                                         )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS server_table_rsa")
        cursor.execute("CREATE TABLE IF NOT EXISTS server (privateKey_1 TEXT,publicKey_1 TEXT,privateKey_2 TEXT,publicKey_2 TEXT,clientPublicKey TEXT)")
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)