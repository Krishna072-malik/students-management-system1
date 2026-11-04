from tkinter import *
import importlib.util
from tkinter import ttk, messagebox
import importlib.util
import sqlite3

from course import courseclass
from student import studentclass 
# Try to import Pillow (PIL)
spec = importlib.util.find_spec("PIL")
if spec is not None:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
else:
    PIL_AVAILABLE = False


class NAME:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1400x700+0+0")
        self.root.config(bg="white")

        # Load top logo
        try:
            if PIL_AVAILABLE:
                pil_image = Image.open("project1.png")
                self.photo = ImageTk.PhotoImage(pil_image)
            else:
                self.photo = PhotoImage(file="project1.png")
        except Exception as e:
            print("Error loading logo image:", e)
            self.photo = None

        # Title bar
        title = Label(
            self.root,
            text="Student Management System",
            image=self.photo,
            compound=LEFT,
            font=("goudy old style", 20, "bold"),
            fg="white",
            bg="blue",
            padx=20,
            height=70
        )
        title.place(x=0, y=0, relwidth=1, height=70)

        # Menu Frame
        m_frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        m_frame.place(x=10, y=80, width=1340, height=80)

        # buttons = ["Course", "Student", "Result", "Logout", "View Results", "Exit"]
        # for i, text in enumerate(buttons):
        #     Button(m_frame, text=text, font=("goudy old style", 15, "bold"),
        #            bg="red", fg="white").place(x=20 + i * 220, y=10, height=40, width=200)
        Button(m_frame, text="Course",command="self.add_course", font=("goudy old style", 15, "bold"), bg="red", fg="white").place(x=20, y=10, height=40, width=200)
        Button(m_frame, text="Student", font=("goudy old style", 15, "bold"), bg="red", fg="white").place(x=240, y=10, height=40, width=200)
        Button(m_frame, text="Result", font=("goudy old style", 15, "bold"), bg="red", fg="white").place(x=460, y=10, height=40, width=200)
        Button(m_frame, text="Logout", font=("goudy old style", 15, "bold"), bg="red", fg="white").place(x=680, y=10, height=40, width=200)
        Button(m_frame, text="View Results", font=("goudy old style", 15, "bold"), bg="red", fg="white").place(x=900, y=10, height=40, width=200)
        Button(m_frame, text="Exit", font=("goudy old style", 15, "bold"), bg="red", fg="white").place(x=1120, y=10, height=40, width=200)

        # Picture section
        try:
            if PIL_AVAILABLE:
                self.project2_img = Image.open("project2.png")
                self.project2_img = self.project2_img.resize((900, 300), Image.Resampling.LANCZOS)
                self.project2_photo = ImageTk.PhotoImage(self.project2_img)
                self.lbl_project2 = Label(self.root, image=self.project2_photo, borderwidth=2, relief=RIDGE)
                self.lbl_project2.place(x=250, y=160, width=900, height=300)
            else:
                print("Pillow not available — skipping image.")
        except Exception as e:
            print("Error loading project2 image:", e)

        # ✅ Always visible stats labels
        self.lbl_course = Label(self.root, text="Total Course\n[ 0 ]",
                                font=("times new roman", 20), bd=10, relief=RIDGE,
                                bg="red", fg="white")
        self.lbl_course.place(x=750, y=550, width=200, height=100)

        self.lbl_student = Label(self.root, text="Total student\n[ 0 ]",
                                 font=("times new roman", 20), bd=10, relief=RIDGE,
                                 bg="#0676ad", fg="white")
        self.lbl_student.place(x=950, y=550, width=200, height=100)

        self.lbl_result = Label(self.root, text="Total result\n[ 0 ]",
                                font=("times new roman", 20), bd=10, relief=RIDGE,
                                bg="#034332", fg="white")
        self.lbl_result.place(x=1150, y=550, width=200, height=100)

        # Footer
        footer = Label(
            self.root,
            text="SMS - Student Management System | Developed by Krishna\nFor any Technical Issue Contact: 9343xx01234",
            font=("goudy old style", 13),
            bg="#262626", fg="white"
        )
        footer.pack(side=BOTTOM, fill=X)


if __name__ == "__main__":
    root = Tk()
    obj = NAME(root)
    root.mainloop()
