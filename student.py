
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class studentclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x500+220+100")
        self.root.config(bg="white")

        # ------------------- VARIABLES -------------------
        self.var_roll = StringVar()
        self.var_Name = StringVar()
        self.var_Email = StringVar()
        self.var_Gender = StringVar()
        self.var_state = StringVar()
        self.var_Address = StringVar()
        self.var_DOB = StringVar()
        self.var_Contact = StringVar()
        self.var_search = StringVar()
        self.var_Admission = StringVar()
        self.var_course = StringVar()
        self.var_City = StringVar()
        self.var_pin = StringVar()

        # ------------------- TITLE -------------------
        title = Label(
            self.root,
            text="Student Management System",
            font=("goudy old style", 20, "bold"),
            bg="#7C9CED",
            fg="white",
        )
        title.pack(side=TOP, fill=X)

        # ------------------- LABELS & ENTRIES -------------------
        # Column 1
        Label(self.root, text="Roll No", font=("goudy old style", 15), bg="white").place(x=10, y=50)
        Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=10, y=90)
        Label(self.root, text="Email", font=("goudy old style", 15), bg="white").place(x=10, y=130)
        Label(self.root, text="Gender", font=("goudy old style", 15), bg="white").place(x=10, y=170)
        Label(self.root, text="State", font=("goudy old style", 15), bg="white").place(x=10, y=210)
        Label(self.root, text="Address", font=("goudy old style", 15), bg="white").place(x=10, y=260)

        self.text_Roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="#F1F1BA")
        self.text_Roll.place(x=130, y=50, width=200)
        self.text_Name = Entry(self.root, textvariable=self.var_Name, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_Name.place(x=130, y=90, width=200)
        self.text_email = Entry(self.root, textvariable=self.var_Email, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_email.place(x=130, y=130, width=200)

        self.text_Gender = ttk.Combobox(
            self.root,
            textvariable=self.var_Gender,
            values=("Select", "Male", "Female", "Other"),
            font=("goudy old style", 15),
            state="readonly",
            justify=CENTER,
        )
        self.text_Gender.place(x=130, y=170, width=200)
        self.text_Gender.current(0)

        self.text_State = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_State.place(x=130, y=210, width=150)

        self.text_Address = Text(self.root, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_Address.place(x=130, y=260, width=500, height=100)

        # Column 2
        Label(self.root, text="D.O.B", font=("goudy old style", 15), bg="white").place(x=350, y=50)
        Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=350, y=90)
        Label(self.root, text="Admission", font=("goudy old style", 15), bg="white").place(x=350, y=130)
        Label(self.root, text="Course", font=("goudy old style", 15), bg="white").place(x=350, y=170)
        Label(self.root, text="City", font=("goudy old style", 15), bg="white").place(x=300, y=210)
        Label(self.root, text="Pin", font=("goudy old style", 15), bg="white").place(x=470, y=210)

        self.text_DOB = Entry(self.root, textvariable=self.var_DOB, font=("goudy old style", 15), bg="#F1F1BA")
        self.text_DOB.place(x=450, y=50, width=200)
        self.text_Contact = Entry(self.root, textvariable=self.var_Contact, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_Contact.place(x=450, y=90, width=200)
        self.text_Admission = Entry(self.root, textvariable=self.var_Admission, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_Admission.place(x=450, y=130, width=200)
        self.text_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_course.place(x=450, y=170, width=200)
        self.text_City = Entry(self.root, textvariable=self.var_City, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_City.place(x=360, y=210, width=100)
        self.text_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_pin.place(x=510, y=210, width=100)

        # ------------------- BUTTONS -------------------
        Button(self.root, text="Add", command=self.add, font=("goudy old style", 15), bg="#4CAF50", fg="white").place(x=130, y=400, width=100, height=40)
        Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#2196F3", fg="white").place(x=240, y=400, width=100, height=40)
        Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white").place(x=350, y=400, width=100, height=40)
        Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white").place(x=460, y=400, width=100, height=40)

        # ------------------- SEARCH PANEL -------------------
        Label(self.root, text="Search By Roll No", font=("goudy old style", 15), bg="white").place(x=700, y=50)
        self.txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15), bg="#F1F1BA")
        self.txt_search.place(x=900, y=50, width=150)
        Button(self.root, text="Search", command=self.search, font=("goudy old style", 15), bg="#4CAF50", fg="white").place(x=1060, y=50, width=100, height=30)

        # ------------------- TABLE FRAME -------------------
        course_frame = Frame(self.root, bd=2, relief=RIDGE)
        course_frame.place(x=700, y=90, width=480, height=340)

        scroll_x = Scrollbar(course_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(course_frame, orient=VERTICAL)
        self.courseTable = ttk.Treeview(
            course_frame,
            columns=("Roll", "Name", "Email", "Gender", "DOB", "Admission", "Contact",
                     "Course", "State", "City", "Pin", "Address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.courseTable.xview)
        scroll_y.config(command=self.courseTable.yview)

        for col in self.courseTable["columns"]:
            self.courseTable.heading(col, text=col)
            self.courseTable.column(col, width=100)
        self.courseTable["show"] = "headings"
        self.courseTable.pack(fill=BOTH, expand=1)
        self.courseTable.bind("<ButtonRelease>", self.get_data)

        self.create_db()
        self.show()

    # ------------------- DATABASE SETUP -------------------
    def create_db(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS student (
                roll TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                gender TEXT,
                dob TEXT,
                admission TEXT,
                contact TEXT,
                course TEXT,
                state TEXT,
                city TEXT,
                pin TEXT,
                address TEXT
            )"""
        )
        con.commit()
        con.close()

    # ------------------- FUNCTIONS -------------------
    def add(self):
        try:
            con = sqlite3.connect("student.db")
            cur = con.cursor()
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number is required", parent=self.root)
                return
            cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row:
                messagebox.showerror("Error", "Roll Number already exists", parent=self.root)
            else:
                cur.execute(
                    "INSERT INTO student (roll, name, email, gender, dob, admission, contact, course, state, city, pin, address) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        self.var_roll.get(),
                        self.var_Name.get(),
                        self.var_Email.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_Admission.get(),
                        self.var_Contact.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_City.get(),
                        self.var_pin.get(),
                        self.text_Address.get("1.0", END),
                    ),
                )
                con.commit()
                messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
                self.show()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        self.courseTable.delete(*self.courseTable.get_children())
        for row in rows:
            self.courseTable.insert("", END, values=row)
        con.close()

    def get_data(self, ev):
        r = self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]
        if not row:
            return
        self.var_roll.set(row[0])
        self.var_Name.set(row[1])
        self.var_Email.set(row[2])
        self.var_Gender.set(row[3])
        self.var_DOB.set(row[4])
        self.var_Admission.set(row[5])
        self.var_Contact.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_City.set(row[9])
        self.var_pin.set(row[10])
        self.text_Address.delete("1.0", END)
        self.text_Address.insert(END, row[11])

    def update(self):
        try:
            con = sqlite3.connect("student.db")
            cur = con.cursor()
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number is required", parent=self.root)
                return
            cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "No student found with this Roll No", parent=self.root)
            else:
                cur.execute(
                    """UPDATE student SET name=?, email=?, gender=?, dob=?, admission=?, contact=?, 
                    course=?, state=?, city=?, pin=?, address=? WHERE roll=?""",
                    (
                        self.var_Name.get(),
                        self.var_Email.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_Admission.get(),
                        self.var_Contact.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_City.get(),
                        self.var_pin.get(),
                        self.text_Address.get("1.0", END),
                        self.var_roll.get(),
                    ),
                )
                con.commit()
                messagebox.showinfo("Success", "Student Updated Successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()

    def delete(self):
        try:
            con = sqlite3.connect("student.db")
            cur = con.cursor()
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number is required", parent=self.root)
                return
            op = messagebox.askyesno("Confirm", "Do you really want to delete this record?", parent=self.root)
            if op:
                cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))
                con.commit()
                messagebox.showinfo("Deleted", "Student deleted successfully", parent=self.root)
                self.show()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.var_roll.set("")
        self.var_Name.set("")
        self.var_Email.set("")
        self.var_Gender.set("Select")
        self.var_DOB.set("")
        self.var_Admission.set("")
        self.var_Contact.set("")
        self.var_course.set("")
        self.var_state.set("")
        self.var_City.set("")
        self.var_pin.set("")
        self.text_Address.delete("1.0", END)

    def search(self):
        try:
            con = sqlite3.connect("student.db")
            cur = con.cursor()
            search_term = self.var_search.get().strip()
            if search_term == "":
                self.show()
                return
            cur.execute("SELECT * FROM student WHERE roll LIKE ?", ('%' + search_term + '%',))
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = studentclass(root)
    root.mainloop()

