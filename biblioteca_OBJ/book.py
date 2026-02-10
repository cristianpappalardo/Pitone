import sqlite3

class Book:
    def __init__(self, isbn, title, author, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies


    @staticmethod
    def get_all_books():
        conn = sqlite3.connect('library.sqlite3')
        cur = conn.cursor()

        try:
            cur.execute('SELECT * FROM books')
            books = cur.fetchall()
            conn.close()
            return books

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []
        

    @staticmethod
    def get_book_from_isbn(isbn):
        conn = sqlite3.connect('library.sqlite3')
        cur = conn.cursor()

        try:
            cur.execute('SELECT * FROM books WHERE isbn = ?', (isbn,))
            book = cur.fetchone()
            conn.close()
            return book

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None

    def add_book(self):
        conn = sqlite3.connect('library.sqlite3')
        cur = conn.cursor()

        try: 
            if Book.get_book_from_isbn(self.isbn) is not None:
                print(f"Book with ISBN {self.isbn} already exists.")
                return
            cur.execute('INSERT INTO books (isbn, title, author, copies) VALUES (?, ?, ?, ?)',
                (self.isbn, self.title, self.author, self.copies))
        
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        
        
