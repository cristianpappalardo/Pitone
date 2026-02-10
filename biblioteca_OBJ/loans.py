import sqlite3

class Loan:
    
    def __init__(self, loan_id, user_id, isbn, loan_date, return_date):
    
        self.user_id = user_id
        self.isbn = isbn
        self.loan_date = loan_date
        self.return_date = return_date
        self.loan_id = loan_id

    def add_loan(self):
        conn = sqlite3.connect('library.sqlite3')
        cur = conn.cursor()

        try: 
            cur.execute('INSERT INTO loans (user_id, isbn, loan_date, return_date) VALUES (?, ?, ?, ?)',
                (self.user_id, self.isbn, self.loan_date, self.return_date))
        
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")


    def add_return(self, return_date):
        conn = sqlite3.connect('library.sqlite3')
        cur = conn.cursor()

        try: 
            cur.execute('UPDATE loans SET return_date = ? WHERE loan_id = ?',
                (return_date, self.loan_id))
        
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")