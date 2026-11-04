# from tkinter import *
# from tkinter import ttk, messagebox
# import sqlite3


# class resultclass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.geometry("1200x500+220+100")
#         self.root.config(bg="white")
        
#         title = Label(
#             self.root,
#             text="Add Student result Management System",
#             font=("goudy old style", 20, "bold"),
#             bg="#88F396",
#             fg="white",
#         )
#         title.pack(side=TOP, fill=X)
        
#         self.var_roll = StringVar()
#         self.var_Name = StringVar()
#         self.var_Email = StringVar()
#         self.var_Gender = StringVar()
#         self.var_state = StringVar()
        
#         Label(self.root, text="Roll No", font=("goudy old style", 15), bg="white").place(x=10, y=50)
#         Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=10, y=90)
#         Label(self.root, text="course", font=("goudy old style", 15), bg="white").place(x=10, y=130)
#         Label(self.root, text="Subject", font=("goudy old style", 15), bg="white").place(x=10, y=170)
#         Label(self.root, text="Subject", font=("goudy old style", 15), bg="white").place(x=10, y=210)
        
#         self.text_Roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="#F1F1BA")
#         self.text_Roll.place(x=130, y=50, width=200)
#         self.text_Name = Entry(self.root, textvariable=self.var_Name, font=("goudy old style", 15), bg="#DAF0C1")
#         self.text_Name.place(x=130, y=90, width=200)
#         self.text_email = Entry(self.root, textvariable=self.var_Email, font=("goudy old style", 15), bg="#DAF0C1")
#         self.text_email.place(x=130, y=130, width=200)
#         self.text_Gender = Entry(self.root, textvariable=self.var_Gender, font=("goudy old style", 15), bg="#DAF0C1")
#         self.text_Gender.place(x=130, y=170, width=200)
#         # self.text_Gender.current(0)

#         self.text_State = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15), bg="#DAF0C1")
#         self.text_State.place(x=130, y=210, width=150)
        
#        
# # buttun
       

# if __name__ == "__main__":
#     root = Tk()
#     obj = resultclass(root)
#     root.mainloop()



# from tkinter import *
# from tkinter import ttk, messagebox

# class resultclass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.geometry("1100x700+220+80")
#         self.root.config(bg="white")

#         title = Label(
#             self.root,
#             text="Add Student Result Management System",
#             font=("goudy old style", 20, "bold"),
#             bg="#88F396",
#             fg="white",
#         )
#         title.pack(side=TOP, fill=X)

#         # ---------- Student Info ----------
#         self.var_roll  = StringVar()
#         self.var_Name = StringVar()
#         self.var_course = StringVar()
#         self.var_branch = StringVar()
#         self.var_state = StringVar()

#         Label(self.root, text="Roll No", font=("goudy old style", 15), bg="white").place(x=10, y=60)
#         Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=10, y=100)
#         Label(self.root, text="Course", font=("goudy old style", 15), bg="white").place(x=360, y=60)
#         Label(self.root, text="Branch", font=("goudy old style", 15), bg="white").place(x=360, y=100)

#         Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="#F1F1BA").place(x=130, y=60, width=200)
#         Entry(self.root, textvariable=self.var_Name, font=("goudy old style", 15), bg="#DAF0C1").place(x=130, y=100, width=200)
#         Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15), bg="#DAF0C1").place(x=450, y=100, width=200)
#         Entry(self.root, textvariable=self.var_branch, font=("goudy old style", 15), bg="#DAF0C1").place(x=450, y=60, width=200)

#         # ---------- Subjects Table ----------
#         Label(self.root, text="Subjects and Marks", font=("goudy old style", 18, "bold"), bg="white", fg="#3B3B3B").place(x=100, y=150)

#         frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
#         frame.place(x=100, y=200, width=700, height=250)

#         # Define columns
#         self.table = ttk.Treeview(frame, columns=("subject", "marks_obtained", "full_marks"), show="headings")
#         self.table.heading("subject", text="Subject Name")
#         self.table.heading("marks_obtained", text="Marks Obtained")
#         self.table.heading("full_marks", text="Full Marks")

#         self.table.column("subject", width=250, anchor=CENTER)
#         self.table.column("marks_obtained", width=150, anchor=CENTER)
#         self.table.column("full_marks", width=150, anchor=CENTER)
#         self.table.pack(fill=BOTH, expand=1)

#         # Add 5 default blank rows
#         for i in range(5):
#             self.table.insert("", END, values=(f"Subject {i+1}", "", ""))

#         # ---------- Entry boxes ----------
#         Label(self.root, text="Subject:", font=("goudy old style", 15), bg="white").place(x=110, y=470)
#         self.var_subject = StringVar()
#         Entry(self.root, textvariable=self.var_subject, font=("goudy old style", 15), bg="#E6F3F0").place(x=200, y=470, width=150)

#         Label(self.root, text="Obtained:", font=("goudy old style", 15), bg="white").place(x=360, y=470)
#         self.var_marks_obtained = StringVar()
#         Entry(self.root, textvariable=self.var_marks_obtained, font=("goudy old style", 15), bg="#E6F3F0").place(x=460, y=470, width=100)

#         Label(self.root, text="Full:", font=("goudy old style", 15), bg="white").place(x=580, y=470)
#         self.var_full_marks = StringVar()
#         Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 15), bg="#E6F3F0").place(x=630, y=470, width=100)

#         Button(self.root, text="Update", font=("goudy old style", 13, "bold"), bg="#2196F3", fg="white",
#                cursor="hand2", command=self.update_row).place(x=750, y=468, width=100, height=30)

#         # ---------- Buttons ----------
#         Button(self.root, text="Add Row", font=("goudy old style", 13, "bold"), bg="#673AB7", fg="white",
#                cursor="hand2", command=self.add_row).place(x=100, y=520, width=120, height=35)

#         Button(self.root, text="Delete Row", font=("goudy old style", 13, "bold"), bg="#F44336", fg="white",
#                cursor="hand2", command=self.delete_row).place(x=240, y=520, width=120, height=35)

#         Button(self.root, text="Calculate Total", font=("goudy old style", 13, "bold"), bg="#9C27B0", fg="white",
#                cursor="hand2", command=self.calculate_total).place(x=380, y=520, width=150, height=35)

#         Button(self.root, text="Save", font=("goudy old style", 13, "bold"), bg="#4CAF50", fg="white",
#                cursor="hand2", command=self.save_result).place(x=550, y=520, width=120, height=35)

#         Button(self.root, text="Submit", font=("goudy old style", 13, "bold"), bg="#FF9800", fg="white",
#                cursor="hand2", command=self.submit_result).place(x=680, y=520, width=120, height=35)
#         Button(self.root, text="View Results", font=("goudy old style", 13, "bold"),
#        bg="#00BCD4", fg="white", cursor="hand2",
#        command=self.view_results_page).place(x=820, y=520, width=150, height=35)


#         # ---------- Totals ----------
#         self.var_total_obtained = StringVar(value="0")
#         self.var_total_full = StringVar(value="0")

#         Label(self.root, text="Total Obtained Marks:", font=("goudy old style", 15, "bold"), bg="white").place(x=300, y=380)
#         Label(self.root, textvariable=self.var_total_obtained, font=("goudy old style", 15), bg="white", fg="#000").place(x=500, y=380)

#         Label(self.root, text="Total Full Marks:", font=("goudy old style", 15, "bold"), bg="white").place(x=600, y=380)
#         Label(self.root, textvariable=self.var_total_full, font=("goudy old style", 15), bg="white", fg="#000").place(x=750, y=380)

#         # Bind selection
#         self.table.bind("<ButtonRelease-1>", self.get_selected_row)
#         self.selected_item = None

#     # ================= FUNCTIONS =====================

#     def get_selected_row(self, event):
#         selected = self.table.focus()
#         data = self.table.item(selected)
#         if data["values"]:
#             self.selected_item = selected
#             subj, marks_obtained, full_marks = data["values"]
#             self.var_subject.set(subj)
#             self.var_marks_obtained.set(marks_obtained)
#             self.var_full_marks.set(full_marks)

#     def update_row(self):
#         if not self.selected_item:
#             messagebox.showerror("Error", "Please select a row first!")
#             return

#         subj = self.var_subject.get().strip()
#         marks_obtained = self.var_marks_obtained.get().strip()
#         full_marks = self.var_full_marks.get().strip()

#         if subj == "" and marks_obtained == "" and full_marks == "":
#             messagebox.showerror("Error", "Please enter details to update!")
#             return

#         self.table.item(self.selected_item, values=(subj, marks_obtained, full_marks))
#         self.var_subject.set("")
#         self.var_marks_obtained.set("")
#         self.var_full_marks.set("")
#         messagebox.showinfo("Success", "Row updated successfully!")

#     def add_row(self):
#         self.table.insert("", END, values=("", "", ""))
#         messagebox.showinfo("Added", "New row added successfully!")

#     def delete_row(self):
#         if not self.selected_item:
#             messagebox.showerror("Error", "Please select a row to delete!")
#             return
#         confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this row?")
#         if confirm:
#             self.table.delete(self.selected_item)
#             self.selected_item = None
#             self.var_subject.set("")
#             self.var_marks_obtained.set("")
#             self.var_full_marks.set("")
#             self.calculate_total()
#             messagebox.showinfo("Deleted", "Row deleted successfully!")

#     def calculate_total(self):
#         """Calculate total obtained and full marks"""
#         total_obt = 0
#         total_full = 0
#         for item in self.table.get_children():
#             values = self.table.item(item)["values"]
#             if len(values) >= 3:
#                 try:
#                     obt = float(values[1]) if values[1] != "" else 0
#                     full = float(values[2]) if values[2] != "" else 0
#                     total_obt += obt
#                     total_full += full
#                 except ValueError:
#                     pass
#         self.var_total_obtained.set(str(total_obt))
#         self.var_total_full.set(str(total_full))

#     def save_result(self):
#         roll = self.var_roll.get()
#         name = self.var_Name.get()
#         if roll == "" or name == "":
#             messagebox.showerror("Error", "Please enter Roll No and Name before saving!")
#             return

#         self.calculate_total()  # auto update totals before saving

#         print("----- Student Result -----")
#         print("Roll:", roll)
#         print("Name:", name)
#         print("Subjects and Marks:")
#         for item in self.table.get_children():
#             subj, marks_obtained, full_marks = self.table.item(item)["values"]
#             print(f"  {subj}: {marks_obtained}/{full_marks}")
#         print(f"Total: {self.var_total_obtained.get()} / {self.var_total_full.get()}")
#         print("--------------------------")

#         messagebox.showinfo("Saved", "Student result saved successfully (check console)")

#     def submit_result(self):
#         self.calculate_total()
#         messagebox.showinfo("Submitted", f"Result submitted successfully!\nTotal: {self.var_total_obtained.get()} / {self.var_total_full.get()}")
        
        
#         def save_result(self):
#            roll = self.var_roll.get()
#            name = self.var_Name.get()
#            if roll == "" or name == "":
#             messagebox.showerror("Error", "Please enter Roll No and Name before saving!")
#         return

#         self.calculate_total()  # auto update totals before saving

#     # Save to file (append mode)
#         with open("results.txt", "a") as f:
#          f.write(f"Roll: {roll}, Name: {name}\n")
#         for item in self.table.get_children():
#             subj, marks_obtained, full_marks = self.table.item(item)["values"]
#             f.write(f"{subj}: {marks_obtained}/{full_marks}\n")
#         f.write(f"Total: {self.var_total_obtained.get()} / {self.var_total_full.get()}\n")
#         f.write("-" * 40 + "\n")

#     messagebox.showinfo("Saved", "Student result saved successfully!\n(Check 'results.txt' file)")


# # Run the app
# if __name__ == "__main__":
#     root = Tk()
#     obj = resultclass(root)
#     root.mainloop()


# from tkinter import *
# from tkinter import ttk, messagebox
# import csv

# class ResultClass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.geometry("1100x700+220+80")
#         self.root.config(bg="white")

#         title = Label(
#             self.root,
#             text="Add Student Result Management System",
#             font=("goudy old style", 20, "bold"),
#             bg="#88F396",
#             fg="white",
#         )
#         title.pack(side=TOP, fill=X)

#         # ---------- Student Info ----------
#         self.var_roll  = StringVar()
#         self.var_Name = StringVar()
#         self.var_course = StringVar()
#         self.var_branch = StringVar()

#         Label(self.root, text="Roll No", font=("goudy old style", 15), bg="white").place(x=10, y=60)
#         Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=10, y=100)
#         Label(self.root, text="Course", font=("goudy old style", 15), bg="white").place(x=360, y=60)
#         Label(self.root, text="Branch", font=("goudy old style", 15), bg="white").place(x=360, y=100)

#         Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="#F1F1BA").place(x=130, y=60, width=200)
#         Entry(self.root, textvariable=self.var_Name, font=("goudy old style", 15), bg="#DAF0C1").place(x=130, y=100, width=200)
#         Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15), bg="#DAF0C1").place(x=450, y=100, width=200)
#         Entry(self.root, textvariable=self.var_branch, font=("goudy old style", 15), bg="#DAF0C1").place(x=450, y=60, width=200)

#         # ---------- Subjects Table ----------
#         Label(self.root, text="Subjects and Marks", font=("goudy old style", 18, "bold"), bg="white", fg="#3B3B3B").place(x=100, y=150)

#         frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
#         frame.place(x=100, y=200, width=700, height=250)

#         self.table = ttk.Treeview(frame, columns=("subject", "marks_obtained", "full_marks"), show="headings")
#         self.table.heading("subject", text="Subject Name")
#         self.table.heading("marks_obtained", text="Marks Obtained")
#         self.table.heading("full_marks", text="Full Marks")

#         self.table.column("subject", width=250, anchor=CENTER)
#         self.table.column("marks_obtained", width=150, anchor=CENTER)
#         self.table.column("full_marks", width=150, anchor=CENTER)
#         self.table.pack(fill=BOTH, expand=1)

#         for i in range(5):
#             self.table.insert("", END, values=(f"Subject {i+1}", "", ""))

#         # ---------- Entry boxes ----------
#         Label(self.root, text="Subject:", font=("goudy old style", 15), bg="white").place(x=110, y=470)
#         self.var_subject = StringVar()
#         Entry(self.root, textvariable=self.var_subject, font=("goudy old style", 15), bg="#E6F3F0").place(x=200, y=470, width=150)

#         Label(self.root, text="Obtained:", font=("goudy old style", 15), bg="white").place(x=360, y=470)
#         self.var_marks_obtained = StringVar()
#         Entry(self.root, textvariable=self.var_marks_obtained, font=("goudy old style", 15), bg="#E6F3F0").place(x=460, y=470, width=100)

#         Label(self.root, text="Full:", font=("goudy old style", 15), bg="white").place(x=580, y=470)
#         self.var_full_marks = StringVar()
#         Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 15), bg="#E6F3F0").place(x=630, y=470, width=100)

#         Button(self.root, text="Update", font=("goudy old style", 13, "bold"), bg="#2196F3", fg="white",
#                cursor="hand2", command=self.update_row).place(x=750, y=468, width=100, height=30)

#         # ---------- Buttons ----------
#         Button(self.root, text="Add Row", font=("goudy old style", 13, "bold"), bg="#673AB7", fg="white",
#                cursor="hand2", command=self.add_row).place(x=100, y=520, width=120, height=35)

#         Button(self.root, text="Delete Row", font=("goudy old style", 13, "bold"), bg="#F44336", fg="white",
#                cursor="hand2", command=self.delete_row).place(x=240, y=520, width=120, height=35)

#         Button(self.root, text="Calculate Total", font=("goudy old style", 13, "bold"), bg="#9C27B0", fg="white",
#                cursor="hand2", command=self.calculate_total).place(x=380, y=520, width=150, height=35)

#         Button(self.root, text="Save", font=("goudy old style", 13, "bold"), bg="#4CAF50", fg="white",
#                cursor="hand2", command=self.save_result).place(x=550, y=520, width=120, height=35)

#         Button(self.root, text="View Results", font=("goudy old style", 13, "bold"),
#                bg="#00BCD4", fg="white", cursor="hand2",
#                command=self.view_results_page).place(x=700, y=520, width=150, height=35)

#         # ---------- Totals ----------
#         self.var_total_obtained = StringVar(value="0")
#         self.var_total_full = StringVar(value="0")

#         Label(self.root, text="Total Obtained Marks:", font=("goudy old style", 15, "bold"), bg="white").place(x=300, y=380)
#         Label(self.root, textvariable=self.var_total_obtained, font=("goudy old style", 15), bg="white", fg="#000").place(x=500, y=380)

#         Label(self.root, text="Total Full Marks:", font=("goudy old style", 15, "bold"), bg="white").place(x=600, y=380)
#         Label(self.root, textvariable=self.var_total_full, font=("goudy old style", 15), bg="white", fg="#000").place(x=750, y=380)

#         self.table.bind("<ButtonRelease-1>", self.get_selected_row)
#         self.selected_item = None

#     # ================= FUNCTIONS =====================
#     def get_selected_row(self, event):
#         selected = self.table.focus()
#         data = self.table.item(selected)
#         if data["values"]:
#             self.selected_item = selected
#             subj, marks_obtained, full_marks = data["values"]
#             self.var_subject.set(subj)
#             self.var_marks_obtained.set(marks_obtained)
#             self.var_full_marks.set(full_marks)

#     def update_row(self):
#         if not self.selected_item:
#             messagebox.showerror("Error", "Please select a row first!")
#             return

#         subj = self.var_subject.get().strip()
#         marks_obtained = self.var_marks_obtained.get().strip()
#         full_marks = self.var_full_marks.get().strip()

#         self.table.item(self.selected_item, values=(subj, marks_obtained, full_marks))
#         self.var_subject.set("")
#         self.var_marks_obtained.set("")
#         self.var_full_marks.set("")

#     def add_row(self):
#         self.table.insert("", END, values=("", "", ""))

#     def delete_row(self):
#         if not self.selected_item:
#             messagebox.showerror("Error", "Please select a row to delete!")
#             return
#         self.table.delete(self.selected_item)
#         self.selected_item = None
#         self.calculate_total()

#     def calculate_total(self):
#         total_obt = 0
#         total_full = 0
#         for item in self.table.get_children():
#             values = self.table.item(item)["values"]
#             if len(values) >= 3:
#                 try:
#                     obt = float(values[1]) if values[1] != "" else 0
#                     full = float(values[2]) if values[2] != "" else 0
#                     total_obt += obt
#                     total_full += full
#                 except ValueError:
#                     pass
#         self.var_total_obtained.set(str(total_obt))
#         self.var_total_full.set(str(total_full))

#     def save_result(self):
#         roll = self.var_roll.get()
#         name = self.var_Name.get()
#         course = self.var_course.get()
#         branch = self.var_branch.get()

#         if roll == "" or name == "":
#             messagebox.showerror("Error", "Please enter Roll No and Name before saving!")
#             return

#         self.calculate_total()

#         with open("results.csv", "a", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow([roll, name, course, branch,
#                              self.var_total_obtained.get(), self.var_total_full.get()])
#         messagebox.showinfo("Saved", "Student result saved successfully!")

#     def view_results_page(self):
#         import view_results
#         view_results.open_results_window(self.root)

# if __name__ == "__main__":
#     root = Tk()
#     obj = ResultClass(root)
#     root.mainloop()


# ===============================
# File: result_entry.py
# ===============================
from tkinter import *
from tkinter import ttk, messagebox
import csv, os

class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Entry")
        self.root.geometry("1100x700+220+80")
        self.root.config(bg="white")

        title = Label(
            self.root,
            text="Student Result Management System - Entry",
            font=("goudy old style", 20, "bold"),
            bg="#88F396",
            fg="white",
        )
        title.pack(side=TOP, fill=X)

        # ---------- Student Info ----------
        self.var_roll  = StringVar()
        self.var_Name = StringVar()
        self.var_course = StringVar()
        self.var_branch = StringVar()

        Label(self.root, text="Roll No", font=("goudy old style", 15), bg="white").place(x=10, y=60)
        Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=10, y=100)
        Label(self.root, text="Course", font=("goudy old style", 15), bg="white").place(x=360, y=60)
        Label(self.root, text="Branch", font=("goudy old style", 15), bg="white").place(x=360, y=100)

        Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="#F1F1BA").place(x=130, y=60, width=200)
        Entry(self.root, textvariable=self.var_Name, font=("goudy old style", 15), bg="#DAF0C1").place(x=130, y=100, width=200)
        Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15), bg="#DAF0C1").place(x=450, y=100, width=200)
        Entry(self.root, textvariable=self.var_branch, font=("goudy old style", 15), bg="#DAF0C1").place(x=450, y=60, width=200)

        # ---------- Subjects Table ----------
        Label(self.root, text="Subjects and Marks", font=("goudy old style", 18, "bold"), bg="white", fg="#3B3B3B").place(x=100, y=150)

        frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        frame.place(x=100, y=200, width=700, height=250)

        self.table = ttk.Treeview(frame, columns=("subject", "marks_obtained", "full_marks"), show="headings")
        self.table.heading("subject", text="Subject Name")
        self.table.heading("marks_obtained", text="Marks Obtained")
        self.table.heading("full_marks", text="Full Marks")
        self.table.pack(fill=BOTH, expand=1)

        for i in range(5):
            self.table.insert("", END, values=(f"Subject {i+1}", "", ""))

        # ---------- Entry boxes ----------
        self.var_subject = StringVar()
        self.var_marks_obtained = StringVar()
        self.var_full_marks = StringVar()

        Label(self.root, text="Subject:", font=("goudy old style", 15), bg="white").place(x=110, y=470)
        Entry(self.root, textvariable=self.var_subject, font=("goudy old style", 15), bg="#E6F3F0").place(x=200, y=470, width=150)

        Label(self.root, text="Obtained:", font=("goudy old style", 15), bg="white").place(x=360, y=470)
        Entry(self.root, textvariable=self.var_marks_obtained, font=("goudy old style", 15), bg="#E6F3F0").place(x=460, y=470, width=100)

        Label(self.root, text="Full:", font=("goudy old style", 15), bg="white").place(x=580, y=470)
        Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 15), bg="#E6F3F0").place(x=630, y=470, width=100)

        Button(self.root, text="Update", font=("goudy old style", 13, "bold"), bg="#2196F3", fg="white",
               cursor="hand2", command=self.update_row).place(x=750, y=468, width=100, height=30)

        # ---------- Buttons ----------
        Button(self.root, text="Add Row", font=("goudy old style", 13, "bold"), bg="#673AB7", fg="white",
               cursor="hand2", command=self.add_row).place(x=100, y=520, width=120, height=35)

        Button(self.root, text="Delete Row", font=("goudy old style", 13, "bold"), bg="#F44336", fg="white",
               cursor="hand2", command=self.delete_row).place(x=240, y=520, width=120, height=35)

        Button(self.root, text="Calculate Total", font=("goudy old style", 13, "bold"), bg="#9C27B0", fg="white",
               cursor="hand2", command=self.calculate_total).place(x=380, y=520, width=150, height=35)

        Button(self.root, text="Save Result", font=("goudy old style", 13, "bold"), bg="#4CAF50", fg="white",
               cursor="hand2", command=self.save_result).place(x=550, y=520, width=150, height=35)

        Button(self.root, text="View Results Page", font=("goudy old style", 13, "bold"),
               bg="#00BCD4", fg="white", cursor="hand2", command=self.open_view_results).place(x=720, y=520, width=180, height=35)

        # ---------- Totals ----------
        self.var_total_obtained = StringVar(value="0")
        self.var_total_full = StringVar(value="0")

        Label(self.root, text="Total Obtained:", font=("goudy old style", 15, "bold"), bg="white").place(x=300, y=380)
        Label(self.root, textvariable=self.var_total_obtained, font=("goudy old style", 15), bg="white", fg="#000").place(x=460, y=380)

        Label(self.root, text="Total Full Marks:", font=("goudy old style", 15, "bold"), bg="white").place(x=600, y=380)
        Label(self.root, textvariable=self.var_total_full, font=("goudy old style", 15), bg="white", fg="#000").place(x=780, y=380)

        self.table.bind("<ButtonRelease-1>", self.get_selected_row)
        self.selected_item = None

    # ================= FUNCTIONS =====================
    def get_selected_row(self, event):
        selected = self.table.focus()
        data = self.table.item(selected)
        if data["values"]:
            self.selected_item = selected
            subj, marks_obtained, full_marks = data["values"]
            self.var_subject.set(subj)
            self.var_marks_obtained.set(marks_obtained)
            self.var_full_marks.set(full_marks)

    def update_row(self):
        if not self.selected_item:
            messagebox.showerror("Error", "Please select a row first!")
            return
        self.table.item(self.selected_item, values=(
            self.var_subject.get(), self.var_marks_obtained.get(), self.var_full_marks.get()
        ))
        self.var_subject.set("")
        self.var_marks_obtained.set("")
        self.var_full_marks.set("")
        self.calculate_total()

    def add_row(self):
        self.table.insert("", END, values=("", "", ""))

    def delete_row(self):
        if not self.selected_item:
            messagebox.showerror("Error", "Please select a row to delete!")
            return
        self.table.delete(self.selected_item)
        self.selected_item = None
        self.calculate_total()

    def calculate_total(self):
        total_obt = total_full = 0
        for item in self.table.get_children():
            values = self.table.item(item)["values"]
            if len(values) == 3:
                try:
                    total_obt += float(values[1] or 0)
                    total_full += float(values[2] or 0)
                except ValueError:
                    pass
        self.var_total_obtained.set(str(total_obt))
        self.var_total_full.set(str(total_full))

    def save_result(self):
        roll = self.var_roll.get().strip()
        name = self.var_Name.get().strip()
        course = self.var_course.get().strip()
        branch = self.var_branch.get().strip()

        if roll == "" or name == "":
            messagebox.showerror("Error", "Please enter Roll No and Name before saving!")
            return

        self.calculate_total()

        os.makedirs("data", exist_ok=True)
        safe_name = "".join(c for c in name if c.isalnum() or c in (" ", "_")).strip().replace(" ", "_")
        file_path = os.path.join("data", f"{roll}_{safe_name}.csv")

        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll No", roll])
            writer.writerow(["Name", name])
            writer.writerow(["Course", course])
            writer.writerow(["Branch", branch])
            writer.writerow([])
            writer.writerow(["Subject", "Marks Obtained", "Full Marks"])
            for item in self.table.get_children():
                writer.writerow(self.table.item(item)["values"])
            writer.writerow([])
            writer.writerow(["Total Obtained", self.var_total_obtained.get()])
            writer.writerow(["Total Full Marks", self.var_total_full.get()])

        messagebox.showinfo("Saved", f"Result saved successfully in file:\n{file_path}")

    def open_view_results(self):
        import result_view
        result_view.open_results_window(self.root)

if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()
