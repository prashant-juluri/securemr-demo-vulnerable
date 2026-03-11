import sqlite3

def search_users(user_input):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE name = '" + user_input + "'"

    cursor.execute(query)

    return cursor.fetchall()