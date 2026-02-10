import sqlite3


class User:
    def __init__(self, user_id, name, surname, email):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email


    def add_user(self):
        conn = sqlite3.connect('library.sqlite3')
        cur = conn.cursor()

        try: 
            cur.execute('INSERT INTO users (name, surname, email) VALUES (?, ?, ?)',
                (self.name, self.surname, self.email))
        
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")


    @staticmethod
    def get_all_users():
        conn = sqlite3.connect('library.sqlite3')
        cur = conn.cursor()

        try:
            cur.execute('SELECT * FROM users')
            users = cur.fetchall()
            conn.close()
            return users

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []        
    
