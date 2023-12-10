from tkinter import*
import tkinter.messagebox  
import Student_Information_BackEnd
from tkinter import ttk
import re

class StudentInfo():
       def __init__(self, master):
              self.master = master
              self.master.title('Student Details')
              self.master.geometry('1350x750')
              self.master.config(bg = 'gray12')
              
              def information():
                     #declare variables
                     self.Name = StringVar()
                     self.Fathers_Name = StringVar()
                     self.Mothers_Name = StringVar()
                     self.Address = StringVar()
                     self.Mobile = StringVar()
                     self.Email = StringVar()
                     self.DOB = StringVar()
                     self.Gender = StringVar()
                     
                     #main functions
                     def StudentRec(event):
                            try: 
                                   global selected_tuple
                                   
                                   index = self.listbox.curselection()[0]
                                   selected_tuple = self.listbox.get(index)

                                   self.Entry_name.delete(0, END)
                                   self.Entry_name.insert(END, selected_tuple[1])
                                   self.Entry_fname.delete(0, END)
                                   self.Entry_fname.insert(END, selected_tuple[2])
                                   self.Entry_mname.delete(0, END)
                                   self.Entry_mname.insert(END, selected_tuple[3])
                                   self.Entry_address.delete(0, END)
                                   self.Entry_address.insert(END, selected_tuple[4])
                                   self.Entry_mobno.delete(0, END)
                                   self.Entry_mobno.insert(END, selected_tuple[5])
                                   self.Entry_emailID.delete(0, END)
                                   self.Entry_emailID.insert(END, selected_tuple[6])
                                   self.Entry_dob.delete(0, END)
                                   self.Entry_dob.insert(END, selected_tuple[7])
                                   self.Entry_gender.delete(0, END)
                                   self.Entry_gender.insert(END, selected_tuple[8])
                            except IndexError:
                                   pass

                     def Add():
                            dob = self.Entry_dob.get()
                            if re.match(r'\d{2}-\d{2}-\d{4}', dob):
                                   if(len(self.Name.get()) != 0):
                                          Student_Information_BackEnd.insert(self.Name.get(), self.Fathers_Name.get(), self.Mothers_Name.get(), self.Address.get(), self.Mobile.get(), self.Email.get(), self.DOB.get(), self.Gender.get())
                                          self.listbox.delete(0, END)
                                          self.listbox.insert(END, (self.Name.get(), self.Fathers_Name.get(), self.Mothers_Name.get(), self.Address.get(), self.Mobile.get(), self.Email.get(), self.DOB.get(), self.Gender.get()))  
                                          tkinter.messagebox.showinfo('Success', 'Data has been added successfully.')
                                   else:
                                          tkinter.messagebox.showerror('Error', 'Name field cannot be empty.')
                            else:
                                   tkinter.messagebox.showerror('Error', 'Invalid DOB. Please enter in DD-MM-YYYY format.')

                     def Display():
                               self.listbox.delete(0, END)
                               for row in Student_Information_BackEnd.view():
                                   self.listbox.insert(END, row, str(' '))


                     def Exit():
                            Exit = tkinter.messagebox.askyesno('Student Details', 'Confirm if you want to exit.')
                            if Exit > 0:
                                   self.master.destroy()
                                   return 
                            

                     def Reset():
                            self.Name.set('')
                            self.Fathers_Name.set('')
                            self.Mothers_Name.set('')
                            self.Address.set('')
                            self.Mobile.set('')
                            self.Email.set('')
                            self.DOB.set('')
                            self.Gender.set('')
                            self.listbox.delete(0, END)
                            Display()

                     

                     def Delete():
                            if(len(self.Name.get()) != 0):
                                   Student_Information_BackEnd.delete(selected_tuple[0])
                                   Reset()
                                   Display()
                                   tkinter.messagebox.showinfo('Success', 'Data has been deleted successfully.')
                            else:
                                   tkinter.messagebox.showerror('Error', 'Name field cannot be empty.')


                     def Search():
                            self.listbox.delete(0, END)
                            search_results = Student_Information_BackEnd.search(self.Name.get(), self.Fathers_Name.get(), self.Mothers_Name.get(), self.Address.get(), self.Mobile.get(), self.Email.get(), self.DOB.get(), self.Gender.get())
                            if search_results:
                                   for row in search_results:
                                          self.listbox.insert(END, row)
                            else:
                                   self.listbox.insert(END, "No results found.")

                     def Update():
                            dob = self.Entry_dob.get()
                            if re.match(r'\d{2}-\d{2}-\d{4}', dob):
                                   if(len(self.Name.get()) != 0):
                                          Student_Information_BackEnd.delete(selected_tuple[0])
                                          Student_Information_BackEnd.insert(self.Name.get(), self.Fathers_Name.get(), self.Mothers_Name.get(), self.Address.get(), self.Mobile.get(), self.Email.get(), self.DOB.get(), self.Gender.get())
                                          self.listbox.delete(0, END)
                                          self.listbox.insert(END, (self.Name.get(), self.Fathers_Name.get(), self.Mothers_Name.get(), self.Address.get(), self.Mobile.get(), self.Email.get(), self.DOB.get(), self.Gender.get()))
                                          tkinter.messagebox.showinfo('Success', 'Data has been updated successfully.')
                                   else:
                                          tkinter.messagebox.showerror('Error', 'Name field cannot be empty.')
                            else:
                                   tkinter.messagebox.showerror('Error', 'Invalid DOB. Please enter in DD-MM-YYYY format.')
                     
                     #Frames

                     self.Main_Frame = LabelFrame(self.master, width = 1200, height = 500, font = ('Sniglet', 20), bg = 'gray12', relief = 'ridge')
                     self.Main_Frame.grid(row = 0, column = 0, padx = 95, pady = 80)

                     self.Frame_1 = LabelFrame(self.Main_Frame, width = 600, height = 400, font = ('Walter Turncoat', 20), relief = 'ridge', bg = 'gray12', text = 'Student Details')
                     self.Frame_1.grid(row = 1, column = 0, padx = 15, pady = 15)

                     self.Frame_2 = LabelFrame(self.Main_Frame, width = 300, height = 400, font = ('Walter Turncoat', 20), relief = 'ridge', bg = 'gray12', text = 'Student Database')
                     self.Frame_2.grid(row = 1, column = 1, padx = 5)                  
                     
                     self.Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('Walter Turncoat', 10), bg = 'gray12', relief = 'ridge')
                     self.Frame_3.grid(row = 2, column = 0, pady = 10)

                     
                     #Labels
                     self.Label_name = Label(self.Frame_1, text = 'Name', fg="white", font = ('Sniglet', 20),  bg = 'gray12')
                     self.Label_name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 5)
                     self.Label_fname = Label(self.Frame_1, text = 'Fathers Name', fg="white", font = ('Sniglet', 20),  bg = 'gray12')
                     self.Label_fname.grid(row = 1, column = 0, sticky = W, padx = 20, pady = 5)
                     self.Label_mname = Label(self.Frame_1, text = 'Mothers Name', fg="white", font = ('Sniglet', 20),  bg = 'gray12')
                     self.Label_mname.grid(row = 2, column = 0, sticky = W, padx = 20, pady = 5)
                     self.Label_address = Label(self.Frame_1, text = 'Address', fg="white", font = ('Sniglet', 20),  bg = 'gray12')
                     self.Label_address.grid(row = 3, column = 0, sticky = W, padx = 20, pady = 5)
                     self.Label_mobno = Label(self.Frame_1, text = 'Mobile Number', fg="white", font = ('Sniglet', 20),  bg = 'gray12')
                     self.Label_mobno.grid(row = 4, column = 0, sticky = W, padx = 20, pady = 5)
                     self.Label_emailID = Label(self.Frame_1, text = 'Email ID', fg="white", font = ('Sniglet', 20),  bg = 'gray12')
                     self.Label_emailID.grid(row = 5, column = 0, sticky = W, padx = 20, pady = 5)
                     self.Label_dob = Label(self.Frame_1, text = 'DOB (DD-MM-YYYY)', fg="white", font = ('Sniglet', 20),  bg = 'gray12')
                     self.Label_dob.grid(row = 6, column = 0, sticky = W, padx = 20, pady = 5)
                     self.Label_gender = Label(self.Frame_1, text = 'Gender', fg="white", font = ('Sniglet', 20),  bg = 'gray12')
                     self.Label_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 5)

                     #Textboxes
                     self.Entry_name = Entry(self.Frame_1, font = ('Sniglet',17), textvariable = self.Name)
                     self.Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
                     self.Entry_fname = Entry(self.Frame_1, font = ('Sniglet',17), textvariable = self.Fathers_Name)
                     self.Entry_fname.grid(row = 1, column = 1, padx = 10, pady = 5)
                     self.Entry_mname = Entry(self.Frame_1, font = ('Sniglet',17), textvariable = self.Mothers_Name)
                     self.Entry_mname.grid(row = 2, column = 1, padx = 10, pady = 5)
                     self.Entry_address = Entry(self.Frame_1, font = ('Sniglet',17), textvariable = self.Address)
                     self.Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
                     self.Entry_mobno = Entry(self.Frame_1, font = ('Sniglet',17), textvariable = self.Mobile)
                     self.Entry_mobno.grid(row = 4, column = 1, padx = 10, pady = 5)
                     self.Entry_emailID = Entry(self.Frame_1, font = ('Sniglet',17), textvariable = self.Email)
                     self.Entry_emailID.grid(row = 5, column = 1, padx = 10, pady = 5)
                     self.Entry_dob = Entry(self.Frame_1, font = ('Sniglet',17), textvariable = self.DOB)
                     self.Entry_dob.grid(row = 6, column = 1, padx = 10, pady = 5)
                     self.Entry_gender = ttk.Combobox(self.Frame_1, values = (' ','Male','Female','Others'), font = ('Sniglet',17), textvariable = self.Gender, width = 19)
                     self.Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)

                     #Buttons
                     self.btnSave = Button(self.Frame_3, text = 'Save', font = ('Walter Turncoat',17), width = 8, command = lambda:[Add(), Display()])
                     self.btnSave.grid(row = 0, column = 0, padx = 14, pady = 10)
                     self.btnDisplay = Button(self.Frame_3, text = 'Display', font = ('Walter Turncoat',17), width = 8, command = Display)
                     self.btnDisplay.grid(row = 0, column = 1, padx = 14, pady = 10)
                     self.btnReset = Button(self.Frame_3, text = 'Reset', font = ('Walter Turncoat',17), width = 8, command = Reset)
                     self.btnReset.grid(row = 0, column = 2, padx = 14, pady = 10)
                     self.btnUpdate = Button(self.Frame_3, text = 'Update', font = ('Walter Turncoat',17), width = 8, command = lambda:[Update(), Display()])
                     self.btnUpdate.grid(row = 0, column = 3, padx = 14, pady = 10)
                     self.btnDelete = Button(self.Frame_3, text = 'Delete', font = ('Walter Turncoat',17), width = 8, command = Delete)
                     self.btnDelete.grid(row = 0, column = 4, padx = 14, pady = 10)
                     self.btnSearch = Button(self.Frame_3, text = 'Search', font = ('Walter Turncoat',17), width = 8, command = Search)
                     self.btnSearch.grid(row = 0, column = 5, padx = 14, pady = 10)
                     self.btnExit = Button(self.Frame_3, text = 'Exit', font = ('Walter Turncoat',17), width = 8, command = Exit)
                     self.btnExit.grid(row = 0, column = 6, padx = 14, pady = 10)

                     #List and Scroll Bar
                     self.scrollbar = Scrollbar(self.Frame_2)
                     self.scrollbar.grid(row = 0, column = 1, sticky = 'ns')

                     self.listbox = Listbox(self.Frame_2, width = 75, height = 19, font = ('Walter Turncoat', 12))
                     self.listbox.bind('<<ListboxSelect>>', StudentRec)
                     self.listbox.grid(row = 0, column = 0)
                     self.scrollbar.config(command = self.listbox.yview)

                     Display()
                            
              information()

root = Tk()
obj = StudentInfo(root)
root.mainloop()
