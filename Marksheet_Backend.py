import sqlite3
import tkinter.messagebox

def connect():
   try:
      con = sqlite3.connect('Marks.db')
      cur = con.cursor()
      cur.execute('CREATE TABLE IF NOT EXISTS Marks (ID INTEGER PRIMARY KEY, Name text, Enroll integer, Fathers_Name text, Mothers_Name text, DOB integer, Gender text, College text, Email text, m1 integer, m2 integer, m3 integer, m4 integer, m5 integer, gt integer, per integer, cgpa integer, grade text, div text, result text)')
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()

def insert(Name = ' ', Enroll = ' ', Fathers_Name = ' ', Mothers_Name = ' ', DOB = ' ', Gender = ' ', College = ' ', Email = ' ', m1 = ' ', m2 = ' ', m3 = ' ', m4 = ' ', m5 = ' ', gt = ' ', per = ' ', cgpa = ' ', grade = ' ', div = ' ', result = ' '):
   try:
      con = sqlite3.connect('Marks.db')
      cur = con.cursor()
      cur.execute('INSERT INTO Marks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Name,Enroll,Fathers_Name,Mothers_Name,DOB,Gender,College,Email,m1,m2,m3,m4,m5,gt,per,cgpa,grade,div,result))
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()

def update(ID, Name, Enroll, Fathers_Name, Mothers_Name, DOB, Gender, College, Email, m1, m2, m3, m4, m5, gt, per, cgpa, grade, div, result):
   try:
      con = sqlite3.connect('Marks.db')
      cursor = con.cursor()
      cursor.execute("UPDATE Marks SET Name = ?, Enroll = ?, Fathers_Name =  ?, Mothers_Name = ?, DOB = ?, Gender = ?, College = ?, Email = ?, m1 = ?, m2 = ?,  m3 = ?, m4 = ?, m5 = ?, gt = ?, per = ?, cgpa = ?, grade = ?, div = ?, result = ? WHERE ID = ?", (Name, Enroll, Fathers_Name, Mothers_Name, DOB, Gender, College, Email, m1, m2, m3, m4, m5, gt, per, cgpa, grade, div, result, ID))
      con.commit()
   except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
   except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
   finally:
      if con:
         con.close()

def search(Enroll):
    try:
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()
       cur.execute('SELECT * FROM Marks WHERE Enroll = ?', (Enroll,))
       row = cur.fetchall()
       return row
    except sqlite3.Error as e:
      tkinter.messagebox.showerror("Database Error", str(e))
      return None
    except Exception as e:
      tkinter.messagebox.showerror("Error", str(e))
      return None
    finally:
       if con:
          con.close() 

connect()

