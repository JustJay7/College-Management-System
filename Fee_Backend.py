import sqlite3
import tkinter.messagebox

def connect():
   try:
      con = sqlite3.connect('fee.db')
      cur = con.cursor()
      cur.execute('CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY, receipt integer, name text, enroll text, date integer, branch text, semester text, total integer, paid integer, balance integer)')
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()

def insert(receipt=' ', name=' ', enroll=' ', date=' ', branch=' ', semester=' ', total=' ', paid=' ', balance=' '):
   try:
      con = sqlite3.connect('fee.db')
      cur = con.cursor()
      cur.execute('INSERT INTO fee VALUES (NULL,?,?,?,?,?,?,?,?,?)', (receipt, name, enroll, date, branch, semester, total, paid, balance))
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
      con = sqlite3.connect('fee.db')
      cur = con.cursor()
      cur.execute('SELECT * FROM fee')
      rows = cur.fetchall()
      return rows
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
      return []
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
      return []
   finally:
      if con:
         con.close()

def delete(id):
   try:
      con = sqlite3.connect('fee.db')
      cur = con.cursor()
      cur.execute('DELETE FROM fee WHERE id = ?',(id,))
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()

def update(id, receipt=' ', name=' ', enroll=' ', date=' ', branch=' ', semester=' ', total=' ', paid=' ', balance=' '):
   try:
      con = sqlite3.connect('fee.db')
      cur = con.cursor()
      cur.execute('UPDATE fee SET receipt = ?, name = ?, enroll = ?, date = ?, branch = ?, semester = ?, total = ?, paid = ?, balance = ? WHERE id = ?', (receipt, name, enroll, date, branch, semester, total, paid, balance, id))
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()

def search(receipt='', name='', enroll='', date='', branch='', semester='', total='', paid='', balance=''):
   try:
      con = sqlite3.connect('fee.db')
      cur = con.cursor()

      query = 'SELECT * FROM fee WHERE'
      params = []
      if receipt:
         query += ' receipt LIKE ? AND'
         params.append('%' + receipt + '%')
      if name:
         query += ' name LIKE ? AND'
         params.append('%' + name + '%')
      if enroll:
         query += ' enroll LIKE ? AND'
         params.append('%' + enroll + '%')
      if date:
         query += ' date LIKE ? AND'
         params.append('%' + date + '%')
      if branch:
         query += ' branch LIKE ? AND'
         params.append('%' + branch + '%')
      if semester:
         query += ' semester LIKE ? AND'
         params.append('%' + semester + '%')
      if total:
         query += ' total = ? AND'
         params.append(total)
      if paid:
         query += ' paid = ? AND'
         params.append(paid)
      if balance:
         query += ' balance = ? AND'
         params.append(balance)

      if params:
         query = query[:-4]
      else:
         query = 'SELECT * FROM fee'

      cur.execute(query, params)
      rows = cur.fetchall()
      return rows
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
      return []
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
      return []
    
connect()