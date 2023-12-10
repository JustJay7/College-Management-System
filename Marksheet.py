from tkinter import*
import Marksheet_Backend
import tkinter.messagebox
from tkinter import ttk

def marksheet(row=None):
       root = Tk()
       root.title('Marksheet')
       root.geometry('1350x750')
       root.config(bg='gray12')

       # Initialize all Tkinter variables
       Name = StringVar(root)
       Enroll = StringVar(root)
       Fathers_Name = StringVar(root)
       Mothers_Name = StringVar(root)
       DOB = StringVar(root)
       Gender = StringVar(root)
       College = StringVar(root)
       Email = StringVar(root)
       m1 = DoubleVar(root)
       m2 = DoubleVar(root)
       m3 = DoubleVar(root)
       m4 = DoubleVar(root)
       m5 = DoubleVar(root)
       gt = DoubleVar(root)
       per = DoubleVar(root)
       cgpa = DoubleVar(root)
       grade = StringVar(root)
       div = StringVar(root)
       result = StringVar(root)

    # Populate data if row is provided
       if row:
              record = row[0]
              Name.set(record[1])
              Enroll.set(record[2])
              Fathers_Name.set(record[3])
              Mothers_Name.set(record[4])
              DOB.set(record[5])
              Gender.set(record[6])
              College.set(record[7])
              Email.set(record[8])
              m1.set(record[9])
              m2.set(record[10])
              m3.set(record[11])
              m4.set(record[12])
              m5.set(record[13])
              gt.set(record[14])
              per.set(record[15])
              cgpa.set(record[16])
              grade.set(record[17])
              div.set(record[18])
              result.set(record[19])

       #==============================================Functions==========================================================
       def Add():
              enroll_number = Enroll.get()
              if len(enroll_number) != 0:
                     existing_record = Marksheet_Backend.search(enroll_number)

                     if existing_record:
                            ID = existing_record[0][0]
                            Marksheet_Backend.update(ID, Name.get(), enroll_number, Fathers_Name.get(), Mothers_Name.get(), DOB.get(), Gender.get(), College.get(), Email.get(), m1.get(), m2.get(), m3.get(), m4.get(), m5.get(), gt.get(), per.get(), cgpa.get(), grade.get(), div.get(), result.get())
                            tkinter.messagebox.showinfo('Success', 'Marks have been updated successfully.')
                     else:
                            Marksheet_Backend.insert(Name.get(), enroll_number, Fathers_Name.get(), Mothers_Name.get(), DOB.get(), Gender.get(), College.get(), Email.get(), m1.get(), m2.get(), m3.get(), m4.get(), m5.get(), gt.get(), per.get(), cgpa.get(), grade.get(), div.get(), result.get())
                            tkinter.messagebox.showinfo('Success', 'Marks have been added successfully.')
              else:
                     tkinter.messagebox.showinfo('Input Error', 'Please enter the Enrollment Number.')


       def Exit():
              Exit = tkinter.messagebox.askyesno('Marksheet','Confirm if you want to Exit')
              if Exit:
                     root.destroy()
                     return

       
       def Compute():
              try:
                     marks = []
                     for entry in [m1, m2, m3, m4, m5]:
                            try:
                                   mark = float(entry.get())
                                   if not (0 <= mark <= 100):
                                          raise ValueError("Marks must be between 0 and 100.")
                                   marks.append(mark)
                            except ValueError:
                                   raise ValueError("Invalid input. Please enter numeric marks between 0 and 100.")

                     x1, x2, x3, x4, x5 = marks
       
                     tot = sum(marks)
                     gt.set(tot)
              
                     Per = (tot * 100) / 500
                     per.set(Per)


                     cg = Per / 9.5
                     cgpa.set(min(round(cg, 1), 10))


                     if per.get() <= 40:
                            grd = 'G'
                     elif per.get() <= 50:
                            grd = 'F'
                     elif per.get() <= 60:
                            grd = 'E'
                     elif per.get() <= 70:
                            grd = 'D'
                     elif per.get() <= 80:
                            grd = 'C'
                     elif per.get() <= 90:
                            grd = 'B'
                     else:
                            grd = 'A'

                     grade.set(grd)

                     count = 0
                     for mark in [x1, x2, x3, x4, x5]:
                            if mark < 33:
                                   count += 1

                     if count == 0:
                            result.set('PASS')
                            if Per <= 45:
                                   div.set('THIRD')
                            elif Per <= 60:
                                   div.set('SECOND')
                            else:
                                   div.set('FIRST')
                     elif count in [1, 2]:
                            result.set('SUPPLY')
                            div.set('') 
                     else:
                            result.set('FAIL')
                            div.set('') 

              except ValueError as e:
                     tkinter.messagebox.showerror('Input Error', str(e))

       def Reset():
              Name.set(' ')
              Enroll.set(' ')
              Fathers_Name.set(' ')
              Mothers_Name.set(' ')
              DOB.set(' ')
              Gender.set(' ')
              College.set(' ')
              Email.set(' ')
              m1.set(0.0)
              m2.set(0.0)
              m3.set(0.0)
              m4.set(0.0)
              m5.set(0.0)
              gt.set(0.0)
              per.set(0.0)
              cgpa.set(0.0)
              grade.set('')
              div.set('')
              result.set('')
       
       #Frame_1 
       Frame_1 = LabelFrame(root, width = 1200, height = 400, font = ('Walter Turncoat', 20), bg = 'gray12', text = 'Student Details', relief = 'ridge')
       Frame_1.grid(row = 1, column = 0, pady = 20, padx = 20)


       #Labels and Entries for Frame_1
       Label_Name = Label(Frame_1, text = 'Name', fg="white", font = ('Sniglet', 17), bg = 'gray12')
       Label_Name.grid(row = 0, column = 0, padx = 80)
       Entry_Name = Entry(Frame_1, font = ('Sniglet', 17), width = 25, textvariable = Name)
       Entry_Name.grid(row = 0, column = 1, padx = 5, pady = 5)

       Label_Enroll = Label(Frame_1, text = 'Enrollment Number', fg="white", font = ('Sniglet', 17), bg = 'gray12')
       Label_Enroll.grid(row = 0, column = 3, padx = 80)
       Entry_Enroll = Entry(Frame_1, font = ('Sniglet', 17), width = 25, textvariable = Enroll)
       Entry_Enroll.grid(row = 0, column = 4, padx = 40)

       Label_Fathers_Name = Label(Frame_1, text = 'Fathers Name', fg="white", font = ('Sniglet', 17), bg = 'gray12')
       Label_Fathers_Name.grid(row = 1, column = 0, padx = 80)
       Entry_Fathers_Name = Entry(Frame_1, font = ('Sniglet', 17), width = 25, textvariable = Fathers_Name)
       Entry_Fathers_Name.grid(row = 1, column = 1, padx = 5, pady = 10)

       Label_Mothers_Name = Label(Frame_1, text = 'Mothers Name', fg="white", font = ('Sniglet', 17), bg = 'gray12')
       Label_Mothers_Name.grid(row = 1, column = 3, padx = 80)
       Entry_Mothers_Name = Entry(Frame_1, font = ('Sniglet', 17), width = 25, textvariable = Mothers_Name)
       Entry_Mothers_Name.grid(row = 1, column = 4, padx = 5)

       Label_DOB = Label(Frame_1, text = 'Date of Birth', fg="white", font = ('Sniglet', 17), bg = 'gray12')
       Label_DOB.grid(row = 2, column = 0, padx = 80)
       Entry_DOB = Entry(Frame_1, font = ('Sniglet', 17), width = 25, textvariable = DOB)
       Entry_DOB.grid(row = 2, column = 1, padx = 5, pady = 5)

       Label_Gender = Label(Frame_1, text = 'Gender', fg="white", font = ('Sniglet', 17), bg = 'gray12')
       Label_Gender.grid(row = 2, column = 3, padx = 80)
       Entry_Gender = ttk.Combobox(Frame_1, values = (' ','Male','Female','Others'), font = ('Sniglet', 17), width = 23, textvariable = Gender, state='readonly')
       Entry_Gender.grid(row = 2, column = 4, padx = 5, pady = 5)

       Label_College = Label(Frame_1, text = 'College Name', fg="white", font = ('Sniglet', 17), bg = 'gray12')
       Label_College.grid(row = 3, column = 0, padx = 80)
       Entry_College = Entry(Frame_1, font = ('Sniglet', 17), width = 25, textvariable = College)
       Entry_College.grid(row = 3, column = 1, padx = 5, pady = 5)

       Label_Email = Label(Frame_1, text = 'College Email ID', fg="white", font = ('Sniglet', 17), bg = 'gray12')
       Label_Email.grid(row = 3, column = 3, padx = 80)
       Entry_Email = Entry(Frame_1, font = ('Sniglet', 17), width = 25, textvariable = Email)
       Entry_Email.grid(row = 3, column = 4, padx = 5, pady = 5)
     
       #Frame_2
       Frame_2 = LabelFrame(root, width = 1200, height = 400, font = ('Walter Turncoat',20), bg = 'gray12', text = 'Grades Obtained', fg="white", relief = 'ridge')
       Frame_2.grid(row = 3, column = 0)

       #Labels for Frame_2
       Label_Subject = Label(Frame_2, text = 'SUBJECT', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_Subject.grid(row = 3, column = 0, padx = 50, pady = 10)

       Label_obt_Marks = Label(Frame_2, text = 'MARKS OBTAINED', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_obt_Marks.grid(row = 3, column = 1, padx = 20)

       Label_Subject = Label(Frame_2, text = 'PASSING MARKS', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_Subject.grid(row = 3, column = 2, padx = 20)

       Label_obt_Marks = Label(Frame_2, text = 'TOTAL MARKS', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_obt_Marks.grid(row = 3, column = 3, padx = 20)

       Label_1 = Label(Frame_2, text = 'MATHEMATICS', fg="white", font = ('Sniglet',15), bg = 'gray12')
       Label_1.grid(row = 4, column = 0)
       Label_2 = Label(Frame_2, text = 'PHYSICS', fg="white", font = ('Sniglet',15), bg = 'gray12')
       Label_2.grid(row = 5, column = 0)
       Label_3 = Label(Frame_2, text = 'CHEMISTRY', fg="white", font = ('Sniglet',15), bg = 'gray12')
       Label_3.grid(row = 6, column = 0)
       Label_4 = Label(Frame_2, text = 'HINDI', fg="white", font = ('Sniglet',15), bg = 'gray12')
       Label_4.grid(row = 7, column = 0)
       Label_5 = Label(Frame_2, text = 'ENGLISH', fg="white", font = ('Sniglet',15), bg = 'gray12')
       Label_5.grid(row = 8, column = 0)
       Label_6 = Label(Frame_2, text = 'GRAND TOTAL', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_6.grid(row = 9, column = 0)
       Label_7 = Label(Frame_2, text = 'PERCENTAGE', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_7.grid(row = 10, column = 0)
       Label_8 = Label(Frame_2, text = 'CGPA', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_8.grid(row = 10, column = 2)
       Label_9 = Label(Frame_2, text = 'GRADE', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_9.grid(row = 10, column = 4)
       Label_10 = Label(Frame_2, text = 'DIVISION', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_10.grid(row = 11, column = 0)
       Label_10 = Label(Frame_2, text = 'RESULT', fg="white", font = ('Walter Turncoat',17), bg = 'gray12')
       Label_10.grid(row = 11, column = 2)
       
       #Entries of Frame_2
       var_1 = StringVar(Frame_2, value = '33')
       var_2 = StringVar(Frame_2, value = '100')
       var_3 = StringVar(Frame_2, value = '500')

       Entry__1 = Entry(Frame_2, font = ('Sniglet',15), width = 5, textvariable = m1)
       Entry__1.grid(row = 4, column = 1)
       Entry__2 = Entry(Frame_2, font = ('Sniglet',15), width = 5, textvariable = m2)
       Entry__2.grid(row = 5, column = 1)
       Entry__3 = Entry(Frame_2, font = ('Sniglet',15), width = 5, textvariable = m3)
       Entry__3.grid(row = 6, column = 1)
       Entry__4 = Entry(Frame_2, font = ('Sniglet',15), width = 5, textvariable = m4)
       Entry__4.grid(row = 7, column = 1)
       Entry__5 = Entry(Frame_2, font = ('Sniglet',15), width = 5, textvariable = m5)
       Entry__5.grid(row = 8, column = 1)
       Entry__6 = Entry(Frame_2, font = ('Sniglet',15), width = 5, textvariable = gt, state = 'readonly')
       Entry__6.grid(row = 9, column = 1, pady = 8)
       Entry__7 = Entry(Frame_2, font = ('Sniglet',15), width = 5, textvariable = per, state = 'readonly')
       Entry__7.grid(row = 10, column = 1, pady = 8)
       Entry__8 = Entry(Frame_2, font = ('Sniglet',15), width = 5, textvariable = cgpa, state = 'readonly')
       Entry__8.grid(row = 10, column = 3, pady = 8)
       Entry__9 = Entry(Frame_2, font = ('Sniglet',15), width = 5, textvariable = grade, state = 'readonly')
       Entry__9.grid(row = 10, column = 5, padx = 20, pady = 8)
       Entry__10 = Entry(Frame_2, font = ('Sniglet',15), width = 8, textvariable = div, state = 'readonly')
       Entry__10.grid(row = 11, column = 1, padx = 20, pady = 8)
       Entry__11 = Entry(Frame_2, font = ('Sniglet',15), width = 7, textvariable = result, state = 'readonly')
       Entry__11.grid(row = 11, column = 3, padx = 20, pady = 8)
       
       Entry_1_2 = Entry(Frame_2, textvariable = var_1, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_1_2.grid(row = 4, column = 2, pady = 5)
       Entry_1_3 = Entry(Frame_2, textvariable = var_2, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_1_3.grid(row = 4, column = 3)
       Entry_2_2 = Entry(Frame_2, textvariable = var_1, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_2_2.grid(row = 5, column = 2, pady = 5)
       Entry_2_3 = Entry(Frame_2, textvariable = var_2, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_2_3.grid(row = 5, column = 3)
       Entry_3_2 = Entry(Frame_2, textvariable = var_1, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_3_2.grid(row = 6, column = 2, pady = 5)
       Entry_3_3 = Entry(Frame_2, textvariable = var_2, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_3_3.grid(row = 6, column = 3)
       Entry_4_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_4_2.grid(row = 7, column = 2, pady = 5)
       Entry_4_3 = Entry(Frame_2, textvariable = var_2, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_4_3.grid(row = 7, column = 3)
       Entry_5_2 = Entry(Frame_2, textvariable = var_1, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_5_2.grid(row = 8, column = 2, pady = 5)
       Entry_5_3 = Entry(Frame_2, textvariable = var_2, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_5_3.grid(row = 8, column = 3)
       Entry_6_3 = Entry(Frame_2, textvariable = var_3, font = ('Sniglet',15), width = 5, state = 'readonly')
       Entry_6_3.grid(row = 9, column = 3)

       #Buttons
       Btn_Compute = Button(Frame_2, text = 'COMPUTE', font = ('Sniglet',15), width = 10, command = Compute)
       Btn_Compute.grid(row = 4, column = 4, padx = 50, pady = 6)
       Btn_Save = Button(Frame_2, text = 'SAVE', font = ('Sniglet',15), width = 10, command = Add)
       Btn_Save.grid(row = 5, column = 4, padx = 50, pady = 6)
       Btn_Cancel = Button(Frame_2, text = 'RESET', font = ('Sniglet',15), width = 10, command = Reset)
       Btn_Cancel.grid(row = 6, column = 4, padx = 50, pady = 6)
       Btn_Exit = Button(Frame_2, text = 'EXIT', font = ('Sniglet',15), width = 10, command = Exit)
       Btn_Exit.grid(row = 7, column = 4, padx = 50, pady = 6)

       root.mainloop()
       
if __name__ == '__main__':
       marksheet()
