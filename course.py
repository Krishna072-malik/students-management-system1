from tkinter import *
from tkinter import ttk, messagebox
import importlib.util
import sqlite3

# Try to import PIL if available
spec = importlib.util.find_spec("PIL")
if spec is not None:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
else:
    PIL_AVAILABLE = False


class courseclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x500+220+100")
        self.root.config(bg="white")

        # Title
        title = Label(
            self.root,
            text="Student Course Management System",
            font=("goudy old style", 20, "bold"),
            bg="#7C9CED",
            fg="white",
        )
        title.pack(side=TOP, fill=X)

        # Variables
        self.var_courseNAME = StringVar()
        self.var_Duration = StringVar()
        self.var_Charges = StringVar()
        self.var_search = StringVar()

        # Labels
        Label(self.root, text="Course Name", font=("goudy old style", 15), bg="white").place(x=10, y=50)
        Label(self.root, text="Duration", font=("goudy old style", 15), bg="white").place(x=10, y=90)
        Label(self.root, text="Charges", font=("goudy old style", 15), bg="white").place(x=10, y=130)
        Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=10, y=160)

        # Entry Fields
        self.text_courseName = Entry(self.root, textvariable=self.var_courseNAME, font=("goudy old style", 15), bg="#F1F1BA")
        self.text_courseName.place(x=130, y=50, width=200)
        self.text_Duration = Entry(self.root, textvariable=self.var_Duration, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_Duration.place(x=130, y=90, width=200)
        self.text_Charges = Entry(self.root, textvariable=self.var_Charges, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_Charges.place(x=130, y=130, width=200)
        self.text_Description = Text(self.root, font=("goudy old style", 15), bg="#DAF0C1")
        self.text_Description.place(x=130, y=160, width=500, height=100)

        # Buttons
        Button(self.root, text="Add", command=self.add, font=("goudy old style", 15), bg="#4CAF50", fg="white").place(x=130, y=280, width=100, height=40)
        Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#2196F3", fg="white").place(x=240, y=280, width=100, height=40)
        Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white").place(x=350, y=280, width=100, height=40)
        Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white").place(x=460, y=280, width=100, height=40)

        # Search Panel
        Label(self.root, text="Search By", font=("goudy old style", 15), bg="white").place(x=700, y=50)
        self.txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15), bg="#F1F1BA")
        self.txt_search.place(x=820, y=50, width=200)
        Button(self.root, text="Search", command=self.search, font=("goudy old style", 15), bg="#4CAF50", fg="white").place(x=1030, y=50, width=100, height=30)

        # Table Frame
        course_frame = Frame(self.root, bd=2, relief=RIDGE)
        course_frame.place(x=700, y=90, width=430, height=340)

        scroll_x = Scrollbar(course_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(course_frame, orient=VERTICAL)
        self.courseTable = ttk.Treeview(
            course_frame,
            columns=("cid", "courseNAME", "Duration", "Charges", "Description"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.courseTable.xview)
        scroll_y.config(command=self.courseTable.yview)

        self.courseTable.heading("cid", text="Course ID")
        self.courseTable.heading("courseNAME", text="Course Name")
        self.courseTable.heading("Duration", text="Duration")
        self.courseTable.heading("Charges", text="Charges")
        self.courseTable.heading("Description", text="Description")
        self.courseTable["show"] = "headings"

        self.courseTable.column("cid", width=50)
        self.courseTable.column("courseNAME", width=120)
        self.courseTable.column("Duration", width=100)
        self.courseTable.column("Charges", width=80)
        self.courseTable.column("Description", width=150)
        self.courseTable.pack(fill=BOTH, expand=1)
        self.courseTable.bind("<ButtonRelease>", self.get_data)

        self.show()

    # # ---------------------- FUNCTIONS ----------------------

    
    def add(self):
      try:
        con = sqlite3.connect(database="db_name.db")
        cur = con.cursor()
        if self.var_courseNAME.get().strip() == "":
            messagebox.showerror("Error", "Course name is required", parent=self.root)
            return

        # Check if already exists
        cur.execute("select * from course where courseNAME=?", (self.var_courseNAME.get(),))
        row = cur.fetchone()
        if row is not None:
            messagebox.showerror("Error", "Course already exists", parent=self.root)
            return

        # Find smallest available cid
        cur.execute("SELECT cid FROM course ORDER BY cid")
        existing_ids = [r[0] for r in cur.fetchall()]
        new_id = 1
        for i in existing_ids:
            if i == new_id:
                new_id += 1
            else:
                break

        # Insert with custom cid
        cur.execute(
            "INSERT INTO course (cid, courseNAME, Duration, Charges, Description) VALUES (?, ?, ?, ?, ?)",
            (
                new_id,
                self.var_courseNAME.get(),
                self.var_Duration.get(),
                self.var_Charges.get(),
                self.text_Description.get("1.0", END),
            ),
        )
        con.commit()
        messagebox.showinfo("Success", f"Course added successfully with ID {new_id}", parent=self.root)
        self.show()
        self.clear()
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)    
        
        
        
        
    def show(self):
        try:
            con = sqlite3.connect(database="db_name.db")
            cur = con.cursor()
            cur.execute("select * from course")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def get_data(self, ev):
        r = self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]
        if not row:
            return
        self.var_courseNAME.set(row[1])
        self.var_Duration.set(row[2])
        self.var_Charges.set(row[3])
        self.text_Description.delete('1.0', END)
        self.text_Description.insert(END, row[4])

    def update(self):
        try:
            con = sqlite3.connect(database="db_name.db")
            cur = con.cursor()
            if self.var_courseNAME.get().strip() == "":
                messagebox.showerror("Error", "Course name is required", parent=self.root)
                return
            cur.execute("select * from course where courseNAME=?", (self.var_courseNAME.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "No such course found!", parent=self.root)
            else:
                cur.execute(
                    "update course set Duration=?, Charges=?, Description=? where courseNAME=?",
                    (
                        self.var_Duration.get(),
                        self.var_Charges.get(),
                        self.text_Description.get("1.0", END),
                        self.var_courseNAME.get(),
                    ),
                )
                con.commit()
                messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def delete(self):
        try:
            con = sqlite3.connect(database="db_name.db")
            cur = con.cursor()
            if self.var_courseNAME.get().strip() == "":
                messagebox.showerror("Error", "Course name is required", parent=self.root)
                return
            op = messagebox.askyesno("Confirm", "Do you really want to delete this course?", parent=self.root)
            if op:
                cur.execute("delete from course where courseNAME=?", (self.var_courseNAME.get(),))
                con.commit()
                messagebox.showinfo("Deleted", "Course deleted successfully", parent=self.root)
                self.show()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def clear(self):
        self.var_courseNAME.set("")
        self.var_Duration.set("")
        self.var_Charges.set("")
        self.text_Description.delete("1.0", END)

    def search(self):
        try:
            con = sqlite3.connect(database="db_name.db")
            cur = con.cursor()
            search_term = self.var_search.get()
            if search_term.strip() == "":
                self.show()
                return
            cur.execute("select * from course where courseNAME LIKE ?", ('%' + search_term + '%',))
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
            
            
            
            def add_course(self):
                self.new_win=Toplevel(self.root)
                self.new_obj=courseclass(self.new_win)


            
        

if __name__ == "__main__":
    root = Tk()
    obj = courseclass(root)
    root.mainloop()
