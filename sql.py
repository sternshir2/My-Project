import sqlite3

class DB:
    def insert_user(self, user_name, user_pass):
        try:
            c = self.conn.cursor()
            c.execute("INSERT INTO users VALUES (?, ?)", (user_name, user_pass))
            self.conn.commit()
            return True
        except(Exception, e):
            print(e)
            return False

    def get_user(self, user_name):
        try:
            c = self.conn.cursor()
            c.execute("SELECT * FROM users WHERE user_name=?", (user_name,))
            return c.fetchone()
        except(Exception, e):
            print(e)
            return False

    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        c = self.conn.cursor()
        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS users (user_name text PRIMARY KEY, password text)''')
