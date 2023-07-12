import sqlite3

def login(username, password):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    if result:
        print("Login successful!")
    else:
        print("Invalid credentials.")

username = input("Username: ")
password = input("Password: ")
login(username, password)
