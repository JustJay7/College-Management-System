from tkinter import*
from tkinter import ttk
from datetime import date, timedelta, datetime
import tkinter.messagebox
import Library_Backend

class Library:
       
       def __init__(self, root):
              self.root = root
              self.root.title('Library Management System')
              self.root.geometry('1350x750')
              self.root.config(bg = 'gray12')

              #Frames
              Main_Frame = Frame(self.root, bg = 'gray12')
              Main_Frame.grid()

              Title_Frame_1 = Frame(Main_Frame, width = 1350, bg = 'gray12', relief = RIDGE, padx = 20)
              Title_Frame_1.pack(side = TOP)

              self.lblTitle = Label(Title_Frame_1, font = ('Walter Turncoat', 30), text = 'Library Management System', fg="white", bg = 'gray12', padx = 13)
              self.lblTitle.grid()

              Button_Frame = Frame(Main_Frame, width = 1350, height = 50, relief = RIDGE, bg = 'gray12')
              Button_Frame.pack(side = BOTTOM)

              Detail_Frame = Frame(Main_Frame, width = 1350, height = 100, relief = RIDGE, bg = 'gray12')
              Detail_Frame.pack(side = BOTTOM)

              Data_Frame = Frame(Main_Frame, width = 1350, height = 400, relief = RIDGE, bg = 'gray12')
              Data_Frame.pack(side = BOTTOM)

              Frame_1 = LabelFrame(Data_Frame, width = 800, height = 400, relief = RIDGE, bg = 'gray12', text = "Library Membership Info:", padx = 5, font = ('Walter Turncoat', 20))
              Frame_1.pack(side = LEFT, padx = 3)

              #Variables
              self.Book_ISBN = StringVar()
              self.Book_Title = StringVar()
              self.Author = StringVar()
              self.Edition = StringVar()
              self.Year = StringVar()
              self.Borrowed = StringVar()
              self.Due = StringVar()
              self.Issued_Days = StringVar()
              self.Overdue = StringVar()
              self.selected_ID = None
              self.initialize_dates()
              self.tree = ttk.Treeview(Detail_Frame)
              self.tree['columns'] = ("ID", "Book_ISBN", "Title", "Author", "Edition", "Year of Publication", "Date Borrowed", "Date Due", "Issued Days", "Overdue Status")
       
              for col in self.tree['columns']:
                     self.tree.heading(col, text=col)
                     self.tree.column(col, width=100)

              self.tree.grid(row=0, column=0, sticky='nsew')
              self.Display()

              #Labels
              self.Label_1 = Label(Frame_1, text = 'Book ISBN', fg="white", font = ('Sniglet', 20), pady = 2, bg = 'gray12' )
              self.Label_1.grid(row = 0, column = 0, sticky = W)
              self.Label_2 = Label(Frame_1, text = 'Book Title', fg="white", font = ('Sniglet', 20), pady = 2, bg = 'gray12' )
              self.Label_2.grid(row = 1, column = 0, sticky = W)
              self.Label_3 = Label(Frame_1, text = 'Author', fg="white", font = ('Sniglet', 20), pady = 2, bg = 'gray12' )
              self.Label_3.grid(row = 2, column = 0, sticky = W)
              self.Label_4 = Label(Frame_1, text = 'Edition', fg="white", font = ('Sniglet', 20), pady = 2, bg = 'gray12' )
              self.Label_4.grid(row = 3, column = 0, sticky = W)
              self.Label_5 = Label(Frame_1, text = 'Year of Publication', fg="white", font = ('Sniglet', 20), pady = 2, bg = 'gray12' )
              self.Label_5.grid(row = 4, column = 0, sticky = W)
              self.Label_6 = Label(Frame_1, text = 'Date Borrowed', fg="white", font = ('Sniglet', 20), pady = 2, bg = 'gray12' )
              self.Label_6.grid(row = 5, column = 0, sticky = W)
              self.Label_7 = Label(Frame_1, text = 'Date Due', fg="white", font = ('Sniglet', 20), pady = 2, bg = 'gray12' )
              self.Label_7.grid(row = 6, column = 0, sticky = W)
              self.Label_8 = Label(Frame_1, text = 'Book issued for', fg="white", font = ('Sniglet', 20), pady = 2, bg = 'gray12' )
              self.Label_8.grid(row = 7, column = 0, sticky = W)
              self.Label_9 = Label(Frame_1, text = 'Overdue Status', fg="white", font = ('Sniglet', 20), pady = 2, bg = 'gray12' )
              self.Label_9.grid(row = 8, column = 0, sticky = W)

              #Entries
              self.Entry_0 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.Book_ISBN)
              self.Entry_0.grid(row = 0, column = 4, padx = 15)
              self.Entry_1 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.Book_Title)
              self.Entry_1.grid(row = 1, column = 4, padx = 15)
              self.Entry_2 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.Author)
              self.Entry_2.grid(row = 2, column = 4, padx = 15)
              self.Entry_3 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.Edition)
              self.Entry_3.grid(row = 3, column = 4, padx = 15)
              self.Entry_4 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.Year)
              self.Entry_4.grid(row = 4, column = 4, padx = 15)
              self.Entry_5 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.Borrowed)
              self.Entry_5.grid(row = 5, column = 4, padx = 15)
              self.Entry_6 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.Due, state='readonly')
              self.Entry_6.grid(row = 6, column = 4, padx = 15)            
              self.Entry_7 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.Issued_Days, state='readonly')
              self.Entry_7.grid(row = 7, column = 4, padx = 15)      
              self.Entry_8 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.Overdue, state='readonly')
              self.Entry_8.grid(row = 8, column = 4, padx = 15)      
                            
              #Listbox and Scrollbar               
              tree_scroll = ttk.Scrollbar(Detail_Frame, orient="vertical", command=self.tree.yview)
              tree_scroll.grid(row=0, column=1, sticky='ns')
              self.tree.configure(yscrollcommand=tree_scroll.set)
              self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

              #Buttons
              Button_1 = Button(Button_Frame, text = 'Save', font = ('Walter Turncoat',17), width = 10, command = lambda:[self.update_issue_info(), self.Insert(), self.Display()])
              Button_1.grid(row = 0, column = 0, padx = 8, pady = 5)
              Button_2 = Button(Button_Frame, text = 'Display', font = ('Walter Turncoat',17), width = 10, command = self.Display)
              Button_2.grid(row = 0, column = 1, padx = 8)
              Button_3 = Button(Button_Frame, text = 'Reset', font = ('Walter Turncoat',17), width = 10, command = lambda: [self.Reset(), self.Display()])
              Button_3.grid(row = 0, column = 2, padx = 8)
              Button_4 = Button(Button_Frame, text = 'Update', font = ('Walter Turncoat',17), width = 10, command = lambda:[self.update_issue_info(), self.Update(), self.Display()])
              Button_4.grid(row = 0, column = 3, padx = 8)
              Button_5 = Button(Button_Frame, text = 'Search', font = ('Walter Turncoat',17), width = 10, command = self.Search)
              Button_5.grid(row = 0, column = 4, padx = 8)
              Button_6 = Button(Button_Frame, text = 'Delete', font = ('Walter Turncoat',17), width = 10, command = lambda: [self.Delete(), self.Display()])
              Button_6.grid(row = 0, column = 5, padx = 8)
              Button_7 = Button(Button_Frame, text = 'Exit', font = ('Walter Turncoat',17), width = 10, command = self.Exit)
              Button_7.grid(row = 0, column = 6, padx = 8)

       #Functions
       def Display(self):
              try:
                     for item in self.tree.get_children():
                            self.tree.delete(item)

                     records = Library_Backend.view()

                     updated_records = []
                     for row in records:
                            due_date_str = row[7]
                            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                            borrowed_date_str = row[6] 
                            borrowed_date = datetime.strptime(borrowed_date_str, "%Y-%m-%d").date()
                            current_date = date.today()

                            overdue_days = (current_date - borrowed_date).days if current_date >= due_date else 0

                            updated_row = list(row)
                            if overdue_days > 0:
                                   updated_row[8] = str(overdue_days) 
                            else:
                                   updated_row[8] = row[8]
                                   
                            if overdue_days > 14:
                                   updated_row[9] = "Overdue" 
                            elif overdue_days == 14:
                                   updated_row[9] = "Due Today"
                            else: 
                                   updated_row[9] = row[9]

                            updated_records.append(updated_row)

                     for updated_row in updated_records:
                            self.tree.insert("", 'end', values=updated_row)
              except Exception as e:
                     tkinter.messagebox.showerror("Error", str(e))

       def refresh_book_list(self, rows):
              try:
                     for i in self.tree.get_children():
                            self.tree.delete(i)

                     for row in rows:
                            if not isinstance(row, (list, tuple)) or not row:
                                   raise ValueError("Invalid row format or empty row.")
                            self.tree.insert("", 'end', values=row)
              except Exception as e:
                     tkinter.messagebox.showerror("Error", str(e))

       def Insert(self):
              try:
                     if len(self.Book_Title.get()) != 0:
                            Library_Backend.insert(self.Book_ISBN.get(), self.Book_Title.get(), self.Author.get(), self.Edition.get(), self.Year.get(), self.Borrowed.get(), self.Due.get(), self.Issued_Days.get(), self.Overdue.get())
                            all_rows = Library_Backend.view()
                            self.refresh_book_list(all_rows)
                            tkinter.messagebox.showinfo("Success", "Book has been inserted successfully.")
                     else:
                            tkinter.messagebox.showerror("Input Error", "Please enter a valid Book Title.")
              except Exception as e:
                     tkinter.messagebox.showerror("Error", str(e))
                                                       
       def Exit(self):
              Exit = tkinter.messagebox.askyesno('Library Management System','Confirm if you want to Exit')
              if Exit:
                     root.destroy()
                     return
                                                               
       def Reset(self):
              self.Book_ISBN.set('')
              self.Book_Title.set('')
              self.Author.set('')
              self.Edition.set('')
              self.Year.set('')
              self.Issued_Days.set('')
              self.Overdue.set('')
              self.initialize_dates()

       def Search(self):
              try:
                     search_results = Library_Backend.search(self.Book_ISBN.get(), self.Book_Title.get(), self.Author.get(), self.Edition.get(), self.Year.get(), self.Borrowed.get()) # Search the database
                     self.refresh_book_list(search_results)
              except Exception as e:
                     tkinter.messagebox.showerror("Error", str(e))

       def update_issue_info(self):
              try:
                     borrowed_date_str = self.Borrowed.get()
                     borrowed_date = datetime.strptime(borrowed_date_str, "%Y-%m-%d").date()
                     due_date = borrowed_date + timedelta(days=14)
                     current_date = date.today()
                     issued_days_count = (current_date - borrowed_date).days

                     self.Issued_Days.set(str(issued_days_count))
                     self.Due.set(str(due_date))

                     if issued_days_count > 14:
                            self.Overdue.set("Overdue")
                     elif issued_days_count == 14:
                            self.Overdue.set("Due Today")
                     else:
                            self.Overdue.set("Not Overdue")
              except ValueError:
                     self.Issued_Days.set("N/A")
                     self.Overdue.set("N/A")
              except Exception as e:
                     tkinter.messagebox.showerror("Error", str(e))
                     self.Issued_Days.set("Error")
                     self.Overdue.set("Error")

       def on_tree_select(self, event):
              try:
                     selected_item = self.tree.selection()

                     if selected_item:
                            item = self.tree.item(selected_item)
                            row = item['values']

                            if len(row) != 10:
                                   raise ValueError("Selected item does not contain the correct number of elements.")

                            self.selected_ID = row[0]
                            self.Book_ISBN.set(row[1])
                            self.Book_Title.set(row[2])
                            self.Author.set(row[3])
                            self.Edition.set(row[4])
                            self.Year.set(row[5])
                            self.Borrowed.set(row[6])
                            
                            self.Entry_6.config(state='normal')
                            self.Due.set(row[7])
                            self.Entry_6.config(state='readonly')

                            self.Issued_Days.set(row[8])
                            self.Overdue.set(row[9])

                            self.update_issue_info()

              except Exception as e:
                     tkinter.messagebox.showerror("Error", str(e))

       def Delete(self):
              try:
                     if self.selected_ID: 
                            Library_Backend.delete(self.selected_ID)
                            all_rows = Library_Backend.view()
                            self.refresh_book_list(all_rows)
                            tkinter.messagebox.showinfo("Success", "Book has been deleted successfully.")
                     else:
                            raise ValueError("No row selected.")
              except Exception as e:
                     tkinter.messagebox.showerror("Error", str(e))


       def Update(self):
              try:
                     if self.selected_ID:
                            Library_Backend.update(self.selected_ID, self.Book_ISBN.get(), self.Book_Title.get(), self.Author.get(), self.Edition.get(), self.Year.get(), self.Borrowed.get(), self.Due.get(), self.Issued_Days.get(), self.Overdue.get())
                            all_rows = Library_Backend.view()
                            self.refresh_book_list(all_rows)
                            tkinter.messagebox.showinfo("Success", "Book has been updated successfully.")
                     else:
                            raise ValueError("No row selected.")
              except Exception as e:
                     tkinter.messagebox.showerror("Error", str(e))

       def initialize_dates(self):
              today = date.today()
              due_date = today + timedelta(days=14)
              self.Due.set(due_date.strftime("%Y-%m-%d"))
              self.Borrowed.set(today.strftime("%Y-%m-%d"))
       
if __name__ == '__main__':
       root = Tk()
       applicaton = Library(root)
       root.mainloop()
