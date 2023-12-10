import sqlite3
import tkinter.messagebox

def connect():
   try:
      con = sqlite3.connect('library.db')
      cur = con.cursor()
      cur.execute('CREATE TABLE IF NOT EXISTS library(ID INTEGER PRIMARY KEY, Book_ISBN text, Book_Title text, Author text, Edition text, Year text, Borrowed integer, Due integer, Issued_Days integer, Overdue text)')
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()

def insert(Book_ISBN = ' ', Book_Title = ' ', Author = ' ', Edition = ' ', Year = ' ', Borrowed = ' ', Due = ' ', Issued_Days = ' ', Overdue = ' '):
   try:
      con = sqlite3.connect('library.db')
      cur = con.cursor()
      cur.execute('INSERT INTO library VALUES (NULL,?,?,?,?,?,?,?,?,?)',(Book_ISBN,Book_Title,Author,Edition,Year,Borrowed,Due,Issued_Days,Overdue))
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()

def view():
   try:
      con = sqlite3.connect('library.db')
      cur = con.cursor()
      cur.execute('SELECT * FROM library')
      rows = cur.fetchall()
      return rows
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
      return None
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
      return None
   finally:
      if con:
         con.close()

def delete(ID):
   try:
      con = sqlite3.connect('library.db')
      cur = con.cursor()
      cur.execute('DELETE FROM library WHERE ID = ?',(ID,))
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()
       
def update(ID, Book_ISBN, Book_Title, Author, Edition, Year, Borrowed, Due, Issued_Days, Overdue):
   try:
      con = sqlite3.connect('library.db')
      cursor = con.cursor()
      cursor.execute("UPDATE library SET Book_ISBN = ?, Book_Title = ?, Author = ?, Edition = ?, Year = ?, Borrowed = ?, Due = ?, Issued_Days = ?, Overdue = ? WHERE ID = ?", (Book_ISBN, Book_Title, Author, Edition, Year, Borrowed, Due, Issued_Days, Overdue, ID))
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()

def search(Book_ISBN='', Book_Title='', Author='', Edition='', Year='', Borrowed=''):
   try:
      con = sqlite3.connect('library.db')
      cur = con.cursor()

      query = 'SELECT * FROM library WHERE'
      params = []
      if Book_ISBN:
         query += ' Book_ISBN LIKE ? AND'
         params.append('%' + Book_ISBN + '%')
      if Book_Title:
         query += ' Book_Title LIKE ? AND'
         params.append('%' + Book_Title + '%')
      if Author:
         query += ' Author LIKE ? AND'
         params.append('%' + Author + '%')
      if Edition:
         query += ' Edition LIKE ? AND'
         params.append('%' + Edition + '%')
      if Year:
         query += ' Year LIKE ? AND'
         params.append('%' + Year + '%')
      if Borrowed:
         query += ' Borrowed LIKE ? AND'
         params.append('%' + Borrowed + '%')

      if params:
         query = query[:-4]
      else:
         query = 'SELECT * FROM library'

      cur.execute(query, params)
      rows = cur.fetchall()
      return rows
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
      return None
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
      return None
connect()
       
       
       
                   
       
