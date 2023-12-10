from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import datetime
import Fee_Backend


class Fee():
    def __init__(self, master):
        self.master = master
        self.master.title('Fee Information')
        self.master.geometry('1350x750')
        self.master.config(bg='gray12')

        #Declaring Variables
        self.receipt = StringVar()
        self.name = StringVar()
        self.enroll = StringVar()
        self.date = StringVar(value=datetime.date.today())
        self.branch = StringVar()
        self.semester = StringVar()
        self.total = DoubleVar()
        self.paid = DoubleVar()
        self.balance = DoubleVar()

        #Functions
        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                self.receipt_entry.delete(0, END)
                self.receipt_entry.insert(END, st[1])
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, st[2])
                self.enroll_entry.delete(0, END)
                self.enroll_entry.insert(END, st[3])
                self.date_entry.delete(0, END)
                self.date_entry.insert(END, st[4])
                self.branch_entry.delete(0, END)
                self.branch_entry.insert(END, st[5])
                self.semester_entry.delete(0, END)
                self.semester_entry.insert(END, st[6])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, st[7])
                self.paid_entry.delete(0, END)
                self.paid_entry.insert(END, st[8])
                self.balance_entry.delete(0, END)
                self.balance_entry.insert(END, st[9])
            except IndexError:
                pass
                
        def View():
            try:
                self.list.delete(0, END)
                for row in Fee_Backend.view():
                    self.list.insert(END, row, str(' '))
            except Exception as e:
                tkinter.messagebox.showerror("Database Error", str(e))
                return

        def Insert():
            if len(self.enroll.get()) != 0:
                try:
                    total_amount = float(self.total.get())
                    paid_amount = float(self.paid.get())
                    balance = total_amount - paid_amount
                    self.balance.set(balance)
                except ValueError:
                    tkinter.messagebox.showerror("Input Error", "Total and Paid fields must be numeric")
                    return

                try:
                    Fee_Backend.insert(self.receipt.get(), self.name.get(), self.enroll.get(), self.date.get(), self.branch.get(), self.semester.get(), self.total.get(), self.paid.get(), self.balance.get())
                    self.list.delete(0, END)
                    self.list.insert(END, (self.receipt.get(), self.name.get(), self.enroll.get(), self.date.get(), self.branch.get(), self.semester.get(), self.total.get(), self.paid.get(), self.balance.get()))
                    tkinter.messagebox.showinfo("Success", "Record has been inserted successfully.")
                except Exception as e:
                    tkinter.messagebox.showerror("Database Error", str(e))
                    return
            else:
                tkinter.messagebox.showerror("Input Error", "Enrollment No. is mandatory.")
                return
            View()

        def Reset():
            self.receipt.set(' ')
            self.name.set(' ')
            self.enroll.set(' ')
            self.date.set(datetime.date.today())
            self.branch.set(' ')
            self.semester.set(' ')
            self.total.set(0.0)
            self.paid.set(0.0)
            self.balance.set(0.0)
            self.Display.delete('1.0', END)
            self.list.delete(0, END)

            View()

        def Delete():
            try:
                Fee_Backend.delete(st[0])
                Reset()
                View()
                tkinter.messagebox.showinfo("Delete", "Record has been deleted successfully.")
            except IndexError:
                tkinter.messagebox.showinfo("Delete Error", "No item selected for deletion.")
            except Exception as e:
                tkinter.messagebox.showerror("Delete Error", str(e))

            View()

        def Search():
            try:
                self.list.delete(0, END)
                for row in Fee_Backend.search(self.receipt.get(), self.name.get(), self.enroll.get(), self.date.get(), self.branch.get(), self.semester.get(), self.total.get(), self.paid.get(), self.balance.get()):
                    self.list.insert(END, row, str(' '))
            except Exception as e:
                tkinter.messagebox.showerror("Search Error", str(e))
                return

        def Update():
            try:
                Fee_Backend.delete(st[0])
                Insert()
                tkinter.messagebox.showinfo("Update", "Record has been updated successfully.")
            except IndexError:
                tkinter.messagebox.showinfo("Update Error", "No item selected for update.")
            except Exception as e:
                tkinter.messagebox.showerror("Update Error", str(e))

            View()

        def Exit():
            Exit = tkinter.messagebox.askyesno('Fee Information', 'Confirm if you want to exit')
            if Exit:
                root.destroy()
                return

        #Frames
        Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('Sniglet', 20), bg = 'gray12', relief = 'ridge')
        Main_Frame.grid(row = 0, column = 0, padx = 80, pady = 80)

        Frame_1 = LabelFrame(Main_Frame, width = 600, height = 400, font = ('Walter Turncoat', 20), relief = 'ridge', bg = 'gray12', text = 'Information')
        Frame_1.grid(row = 1, column = 0, padx = 15, pady = 15)

        Frame_2 = LabelFrame(Main_Frame, width = 750, height = 400, font = ('Walter Turncoat', 20), relief = 'ridge', bg = 'gray12', text = 'Fee Database')
        Frame_2.grid(row = 1, column = 1, padx = 5)

        Button_Frame = LabelFrame(master, width = 1200, height = 100, bg = 'gray12', relief = 'ridge')
        Button_Frame.grid(row = 2, column = 0, pady = 10)

        #Labels using Frames
        self.receipt_label = Label(Frame_1, text='Receipt No. : ', fg="white", font=('Sniglet', 20), bg='gray12')
        self.receipt_label.grid(row=0, column=0, padx=15, sticky=W)

        self.name_label = Label(Frame_1, text='Student Name : ', fg="white", font=('Sniglet', 20), bg='gray12')
        self.name_label.grid(row=1, column=0, padx=15, sticky=W)

        self.enroll_label = Label(Frame_1, text='Enrollment No. : ', fg="white", font=('Sniglet', 20), bg='gray12')
        self.enroll_label.grid(row=2, column=0, padx=15, sticky=W)

        self.Date_label = Label(Frame_1, text='Date : ', fg="white", font=('Sniglet', 20), bg='gray12')
        self.Date_label.grid(row=3, column=0, padx=15, sticky=W)

        self.branch_label = Label(Frame_1, text='Branch : ', fg="white", font=('Sniglet', 20), bg='gray12')
        self.branch_label.grid(row=4, column=0, padx=15, sticky=W)

        self.semester_label = Label(Frame_1, text='Semester : ', fg="white", font=('Sniglet', 20), bg='gray12')
        self.semester_label.grid(row=5, column=0, padx=15, sticky=W)

        self.total_label = Label(Frame_1, text='TOTAL AMOUNT : ', fg="white", font=('Sniglet', 20), bg='gray12')
        self.total_label.grid(row=6, column=0, padx=15, sticky=W)

        self.paid_label = Label(Frame_1, text='PAID AMOUNT : ', fg="white", font=('Sniglet', 20), bg='gray12')
        self.paid_label.grid(row=7, column=0, padx=15, sticky=W)

        self.balance_label = Label(Frame_1, text='BALANCE DUE : ', fg="white", font=('Sniglet', 20), bg='gray12')
        self.balance_label.grid(row=8, column=0, padx=15, sticky=W)

        #Entries using Frames
        self.receipt_entry = Entry(Frame_1, font=('Sniglet', 17), textvariable=self.receipt)
        self.receipt_entry.grid(row=0, column=1, padx=15, pady=5)

        self.name_entry = Entry(Frame_1, font=('Sniglet', 17), textvariable=self.name)
        self.name_entry.grid(row=1, column=1, padx=15, pady=5)

        self.enroll_entry = Entry(Frame_1, font=('Sniglet', 17), textvariable=self.enroll)
        self.enroll_entry.grid(row=2, column=1, padx=15, pady=5)

        self.date_entry = Entry(Frame_1, font=('Sniglet', 17), textvariable=self.date)
        self.date_entry.grid(row=3, column=1, padx=15, pady=5)

        self.branch_entry = ttk.Combobox(Frame_1, values=(' ', 'CSE', 'IT', 'ETC/ET&T', 'Mechanical', 'Civil', 'EE', 'EEE'), font=('Sniglet', 17), width=19, textvariable=self.branch)
        self.branch_entry.grid(row=4, column=1, padx=15, pady=5)

        self.semester_entry = ttk.Combobox(Frame_1, values=(' ', 'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH', 'SEVENTH', 'EIGHTH'), font=('Sniglet', 17), width=19, textvariable=self.semester)
        self.semester_entry.grid(row=5, column=1, padx=15, pady=5)

        self.total_entry = Entry(Frame_1, font=('Sniglet', 17), width=20, textvariable=self.total)
        self.total_entry.grid(row=6, column=1, padx=15, pady=5)

        self.paid_entry = Entry(Frame_1, font=('Sniglet', 17), width=20, textvariable=self.paid)
        self.paid_entry.grid(row=7, column=1, padx=15, pady=5)

        self.balance_entry = Entry(Frame_1, font=('Sniglet', 17), width=20, textvariable=self.balance, state='readonly')
        self.balance_entry.grid(row=8, column=1, padx=15, pady=5)

        #Frame_2
        self.Display = Text(Frame_2, width=42, height=12, font=('Sniglet', 20))
        self.Display.grid(row=0, column=0, padx=3)

        #List and Scroll Bar
        sb = Scrollbar(Frame_2)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(Frame_2, font = ('Walter Turncoat', 12), width=75, height=19)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0)
        sb.config(command=self.list.yview)

        #Buttons
        btnSave = Button(Button_Frame, text = 'Save', font = ('Walter Turncoat',17), width = 8, command = Insert)
        btnSave.grid(row = 0, column = 0, padx = 14, pady = 10)

        btnDisplay = Button(Button_Frame, text = 'Display', font = ('Walter Turncoat',17), width = 8, command = View)
        btnDisplay.grid(row = 0, column = 1, padx = 14, pady = 10)

        btnReset = Button(Button_Frame, text = 'Reset', font = ('Walter Turncoat',17), width = 8, command = Reset)
        btnReset.grid(row = 0, column = 2, padx = 14, pady = 10)

        btnUpdate = Button(Button_Frame, text = 'Update', font = ('Walter Turncoat',17), width = 8, command = Update)
        btnUpdate.grid(row = 0, column = 3, padx = 14, pady = 10)

        btnDelete = Button(Button_Frame, text = 'Delete', font = ('Walter Turncoat',17), width = 8, command=Delete)
        btnDelete.grid(row = 0, column = 4, padx = 14, pady = 10)

        btnSearch = Button(Button_Frame, text = 'Search', font = ('Walter Turncoat',17), width = 8, command = Search)
        btnSearch.grid(row = 0, column = 5, padx = 14, pady = 10)

        btnExit = Button(Button_Frame, text = 'Exit', font = ('Walter Turncoat',17), width = 8, command = Exit)
        btnExit.grid(row = 0, column = 6, padx = 14, pady = 10)

        View()

root = Tk()
obj = Fee(root)
root.mainloop()
