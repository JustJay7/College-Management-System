import sqlite3

def connect():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS student (ID INTEGER PRIMARY KEY, Name text, Fathers_Name text, Mothers_Name text, Address text, Mobile integer, Email text, DOB integer, Gender text)")

       conn.commit()
       conn.close()

def insert(Name = " ", Fathers_Name = " ", Mothers_Name = " ", Address = " ", Mobile = " ", Email = " ", DOB = " ", Gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)", (Name, Fathers_Name, Mothers_Name, Address , Mobile, Email, DOB, Gender))

       conn.commit()
       conn.close()
                                                                        
def view():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(ID):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM student WHERE ID = ?", (ID,))

       conn.commit()
       conn.close()

def update(ID,Name = " ", Fathers_Name = " ", Mothers_Name = " ", Address = " ", Mobile = " ", Email = " ", DOB = " ", Gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("UPDATE student SET Name = ? OR Fathers_Name = ? OR Mothers_Name = ? OR Address = ? OR Mobile = ? OR Email = ? OR DOB = ? OR Gender = ?", \
                   (Name, Fathers_Name, Mothers_Name, Address , Mobile, Email, DOB, Gender))

       conn.commit()
       conn.close()

def search(Name="", Fathers_Name="", Mothers_Name="", Address="", Mobile="", Email="", DOB="", Gender=""):
       con = sqlite3.connect("student.db")
       cur = con.cursor()

       query = "SELECT * FROM student WHERE"
       params = []
       if Name:
              query += ' Name LIKE ? AND'
              params.append('%' + Name + '%')
       if Fathers_Name:
              query += ' Fathers_Name LIKE ? AND'
              params.append('%' + Fathers_Name + '%')
       if Mothers_Name:
              query += ' Mothers_Name LIKE ? AND'
              params.append('%' + Mothers_Name + '%')
       if Address:
              query += ' Address LIKE ? AND'
              params.append('%' + Address + '%')
       if Mobile:
              query += ' Mobile LIKE ? AND'
              params.append('%' + Mobile + '%')
       if Email:
              query += ' Email LIKE ? AND'
              params.append('%' + Email + '%')
       if DOB:
              query += ' DOB LIKE ? AND'
              params.append('%' + DOB + '%')
       if Gender:
              query += ' Gender = ? AND'
              params.append(Gender)

       # Remove the trailing ' AND'
       if params:
              query = query[:-4]
       else:
              query = 'SELECT * FROM fee'

       cur.execute(query, params)
       rows = cur.fetchall()
       con.close()
       return rows
                                                               
connect()
       
