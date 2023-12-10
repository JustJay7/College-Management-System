from tkinter import * 
import Marksheet_Backend
import Marksheet
import tkinter.messagebox
from Marksheet import marksheet

class Window_1():
       def __init__(self, master):
              self.master = master
              self.master.title('Marksheet Search Page')
              self.master.geometry('1350x750')
              self.master.config(bg = 'gray12')

              self.Enroll = StringVar()
              frame = LabelFrame(self.master, width = 1000, height = 100, font = ('Sniglet', 20), relief = 'ridge', bg = 'gray12')
              frame.grid(row = 1, column = 0, padx = 300, pady = 250)

              label = Label(frame, text = 'Enter Roll Number:', fg="white", font = ('Walter Turncoat', 20), bg = 'gray12' )
              label.grid(row = 0, column = 0, padx = 100, pady = 10)

              entry = Entry(frame, font = ('Sniglet', 20), textvariable = self.Enroll)
              entry.grid(row = 0, column = 1, padx = 30, pady = 20)

              def Search():
                     roll_number = self.Enroll.get()

                     if len(roll_number) != 0:
                            existing_record = Marksheet_Backend.search(roll_number)

                            if existing_record:
                                   marksheet(existing_record)
                            else:
                                   tkinter.messagebox.showinfo('No Record Found', 'No records found for the given Roll No.')
                     else:
                            tkinter.messagebox.askokcancel('Attention', 'Please enter a valid Roll No.')
                            return

              def new():
                     roll_number = self.Enroll.get()

                     if len(roll_number) != 0:
                            existing_record = Marksheet_Backend.search(roll_number)
                            if existing_record:
                                   tkinter.messagebox.showerror('Error', 'A marksheet already exists for this Roll No.')
                            else:
                                   Marksheet.marksheet()
                     else:
                            tkinter.messagebox.showerror('Error', 'Please enter a valid Roll No.')
   
              btnSearch = Button(frame, text = 'Search', width = 15, font = ('Walter Turncoat',17), command=Search)
              btnSearch.grid(row = 1, column = 0, padx = 50)
              btnNew = Button(frame, text = 'Create New', width = 15, font = ('Walter Turncoat',17), command=new)
              btnNew.grid(row = 1, column = 1, padx = 50, pady = 20 )

root = Tk()
root.title('Search Page')
Window_1(root)
root.mainloop()
