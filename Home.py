
from tkinter import *
from tkinter import ttk, messagebox
import importlib.util
import sqlite3, csv, os
from course import courseclass
from student import studentclass
from result import ResultClass
from viewresult import open_results_window

# PIL check
spec = importlib.util.find_spec("PIL")
if spec is not None:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
else:
    PIL_AVAILABLE = False

class SMS_Dashboard: # Renamed class from 'NAME' to 'SMS_Dashboard'
    def __init__(self, root):
        self.root = root
        # self.root.title("Student Management System Dashboard")
        self.root.geometry("1400x700+0+0")
        self.root.config(bg="#f3f9fb") # Light gray background for a modern feel
        self.root.focus_force()

        # --- Define Color Palette ---
        self.primary_color = "#0e7ff0"  # Dark blue-gray for main elements
        self.accent_color = "#6783bf"   # Facebook-like blue for highlights
        self.text_color = "white"
        self.card_bg = "white"

        # --------------------------
        #   TITLE BAR (HEADER)
        # --------------------------
        header_frame = Frame(self.root, bg=self.primary_color, height=60)
        header_frame.pack(side=TOP, fill=X)
        
        # Load image for title left
        self.title_logo = None
        try:
            if PIL_AVAILABLE:
                img = Image.open("screenshot1.png") # Ensure this file exists
                img = img.resize((45, 45), Image.Resampling.LANCZOS)
                self.title_logo = ImageTk.PhotoImage(img)
            else:
                self.title_logo = PhotoImage(file="screenshot1.png") # Ensure this file exists
        except Exception as e:
            # print(f"Could not load logo image: {e}")
            pass # Keep running even if image fails

        # Show logo at LEFT
        if self.title_logo:
            Label(header_frame, image=self.title_logo, bg=self.primary_color).pack(side=LEFT, padx=20)

        # Title text next to image
        Label(
            header_frame,
            text="Student Result Management System Dashboard",
            font=("Helvetica", 20, "bold"),
            fg=self.text_color,
            bg=self.primary_color
        ).pack(side=LEFT, padx=20)
        
        # --------------------------
        #        MENU BAR
        # --------------------------
        # Replaced LabelFrame with a simple Frame for a cleaner horizontal menu bar
        m_frame = Frame(self.root, bg=self.card_bg, height=60)
        m_frame.place(x=20, y=60, relwidth=1, ) # Positioned directly below the header

        # Unified button style
        btn_style = {
            "font": ("Helvetica", 12, "bold"),
            "bg": self.accent_color,
            "fg": self.text_color,
            
            "bd": 0,
            "cursor": "hand2",
            "activebackground": "#313F63" # Slightly lighter color when clicked
        }
        
        # Using pack/grid for cleaner menu alignment within the bar
        Button(m_frame, text="Course", command=self.add_course, **btn_style, border=5).pack(side=LEFT, padx=20, pady=10, ipady=5, ipadx=10)
        Button(m_frame, text="Student", command=self.add_student, **btn_style,border=5 ).pack(side=LEFT, padx=20, pady=10, ipady=5, ipadx=10)
        Button(m_frame, text="Result Entry", command=self.add_result, **btn_style,border=5).pack(side=LEFT, padx=20, pady=10, ipady=5, ipadx=10)
        Button(m_frame, text="View Results", command=self.add_viewresult, **btn_style,border=5).pack(side=LEFT, padx=20, pady=10, ipady=5, ipadx=10)
        Button(m_frame, text="Logout", **btn_style, border=5).pack(side=LEFT, padx=20, pady=10, ipady=5, ipadx=10)
        Button(m_frame, text="Exit", command=self.root.destroy, **btn_style, border=5).pack(side=LEFT, padx=20, pady=10, ipady=5, ipadx=10)


        # --------------------------
        #       MAIN CONTENT AREA (IMAGE & STATS)
        # --------------------------
        content_y_start = 140
        content_height = 530

        # Main image placeholder (Using 'project2.png' from original code)
        try:
            if PIL_AVAILABLE:
                project2_img = Image.open("project2.png") # Ensure thisgit
                # Used a Frame for better border control
                img_frame = Frame(self.root, bd=2, relief=RIDGE, bg=self.card_bg)
                img_frame.place(x=70, y=content_y_start, width=1000, height=content_height)
                Label(img_frame, image=self.project2_photo).pack(fill=BOTH, expand=True)

        except Exception as e:
            print("Error loading project2 image:", e)
            # Placeholder label if image fails to load
            Label(self.root, text="[ Dashboard Main Image Area ]", bg=self.card_bg, font=("Helvetica", 20)).place(x=70, y=content_y_start, width=1000, height=content_height)


        # --------------------------
        #        STATS BOXES (Cards on the right)
        # --------------------------
        stats_x = 1150
        stats_width = 200
        stats_height = 100

        # Card 1: Courses
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]",
                                font=("Helvetica", 18, "bold"), bd=0, # Removed bulky border
                                relief=FLAT, bg="#e74c3c", fg=self.text_color, # Flat color (Red)
                                pady=15)
        self.lbl_course.place(x=stats_x, y=content_y_start + 30, width=stats_width, height=stats_height)

        # Card 2: Students
        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]",
                                 font=("Helvetica", 18, "bold"), bd=0,
                                 relief=FLAT, bg="#3498db", fg=self.text_color, # Flat color (Blue)
                                 pady=15)
        self.lbl_student.place(x=stats_x, y=content_y_start + 180, width=stats_width, height=stats_height)

        # Card 3: Results
        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]",
                                font=("Helvetica", 18, "bold"), bd=0,
                                relief=FLAT, bg="#2ecc71", fg=self.text_color, # Flat color (Green)
                                pady=15)
        self.lbl_result.place(x=stats_x, y=content_y_start + 330, width=stats_width, height=stats_height)

        # --------------------------
        #          FOOTER
        # --------------------------
        footer_bg = "#2c3e50" # Darker blue-gray
        footer = Label(self.root,
                       text="SMS - Student Management System | Developed by Krishna\nFor any Technical Issue Contact: 9343xx01234",
                       font=("Helvetica", 10),
                       bg=footer_bg, fg="white", height=3)
        footer.pack(side=BOTTOM, fill=X)
        
        # NOTE: You might want to add a function here like update_stats()
        # and call it periodically to update the [ 0 ] values from your database.


    # MENU FUNCTIONS remain the same as they call your other modules
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.app = courseclass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.app = studentclass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.app = ResultClass(self.new_win)

    def add_viewresult(self):
        self.new_win = Toplevel(self.root)
        self.app = open_results_window(self.new_win)
        
        


# MAIN EXECUTION
if __name__ == "__main__":
    root = Tk()
    # Updated class name here
    obj = SMS_Dashboard(root) 
    root.mainloop();
    






























# from tkinter import *
# from course import courseclass
# from student import studentclass
# from result import ResultClass
# from viewresult import open_results_window
# from tkinter import ttk, messagebox
# import importlib.util
# import sqlite3, csv, os

# # PIL check
# spec = importlib.util.find_spec("PIL")
# if spec is not None:
#     from PIL import Image, ImageTk
#     PIL_AVAILABLE = True
# else:
#     PIL_AVAILABLE = False


# class NAME:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.geometry("1400x700+0+0")
#         self.root.config(bg="white")
#         self.root.focus_force()

#         # --------------------------
#         #   TITLE WITH IMAGE (LEFT)
#         # --------------------------
#         title_frame = Frame(self.root, bg="blue")
#         title_frame.place(x=0, y=0, relwidth=1, height=60)
        
#         center_frame = Frame(title_frame, bg="blue")
#         center_frame.place(relx=0.5, rely=0.5, anchor="center")

#         # Load image for title left
#         self.title_logo = None
#         try:
#             if PIL_AVAILABLE:
#                 img = Image.open("screenshot1.png")
#                 img = img.resize((45, 45), Image.Resampling.LANCZOS)
#                 self.title_logo = ImageTk.PhotoImage(img)
#             else:
#                 self.title_logo = PhotoImage(file="screenshot1.png")
#         except:
#             self.title_logo = None

#         # Show logo at LEFT
#         if self.title_logo:
#             Label(title_frame, image=self.title_logo, bg="blue").pack( side=LEFT, padx=10, )

#         # Title text next to image
#         Label(
#             title_frame,
#             text="Student Result Management System",
#             font=("goudy old style", 22, "bold"),
#             fg="white",
#             bg="blue"
#         ).pack(  padx=10, anchor="center")

#         # --------------------------
#         #        MENU FRAME
#         # --------------------------
#         m_frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
#         m_frame.place(x=70, y=70, width=1340, height=80)

#         Button(m_frame, text="Course", font=("goudy old style", 15, "bold"),
#                bg="red", fg="white", command=self.add_course).place(x=20, y=10, height=40, width=200)

#         Button(m_frame, text="Student", font=("goudy old style", 15, "bold"),
#                bg="red", fg="white", command=self.add_student).place(x=240, y=10, height=40, width=200)

#         Button(m_frame, text="Result", font=("goudy old style", 15, "bold"),
#                bg="red", fg="white", command=self.add_result).place(x=460, y=10, height=40, width=200)

#         Button(m_frame, text="View Results", font=("goudy old style", 15, "bold"),
#                bg="red", fg="white", command=self.add_viewresult).place(x=680, y=10, height=40, width=200)

#         Button(m_frame, text="Logout", font=("goudy old style", 15, "bold"),
#                bg="red", fg="white").place(x=900, y=10, height=40, width=200)

#         Button(m_frame, text="Exit", font=("goudy old style", 15, "bold"),
#                bg="red", fg="white", command=self.root.destroy).place(x=1120, y=10, height=40, width=200)

#         # --------------------------
#         #       PROJECT2 IMAGE
#         # --------------------------
#         try:
#             if PIL_AVAILABLE:
#                 project2_img = Image.open("project2.png")
#                 project2_img = project2_img.resize((1000, 500), Image.Resampling.LANCZOS)
#                 self.project2_photo = ImageTk.PhotoImage(project2_img)

#                 Label(self.root, image=self.project2_photo, borderwidth=2, relief=RIDGE)\
#                     .place(x=70, y=170, width=1000, height=500)

#         except Exception as e:
#             print("Error loading project2 image:", e)

#         # --------------------------
#         #        STATS BOXES
#         # --------------------------
#         self.lbl_course = Label(self.root, text="Total Course\n[ 0 ]",
#                                 font=("times new roman", 20), bd=10,
#                                 relief=RIDGE, bg="red", fg="white")
#         self.lbl_course.place(x=1150, y=200, width=200, height=100)

#         self.lbl_student = Label(self.root, text="Total Student\n[ 0 ]",
#                                  font=("times new roman", 20), bd=10,
#                                  relief=RIDGE, bg="#0676ad", fg="white")
#         self.lbl_student.place(x=1150, y=350, width=200, height=100)

#         self.lbl_result = Label(self.root, text="Total Result\n[ 0 ]",
#                                 font=("times new roman", 20), bd=10,
#                                 relief=RIDGE, bg="#034332", fg="white")
#         self.lbl_result.place(x=1150, y=500, width=200, height=100)

#         # --------------------------
#         #          FOOTER
#         # --------------------------
#         footer = Label(self.root,
#                        text="SMS - Student Management System | Developed by Krishna\nFor any Technical Issue Contact: 9343xx01234",
#                        font=("goudy old style", 13),
#                        bg="#262626", fg="white")
#         footer.pack(side=BOTTOM, fill=X)

#     # MENU FUNCTIONS
#     def add_course(self):
#         self.new_win = Toplevel(self.root)
#         self.app = courseclass(self.new_win)

#     def add_student(self):
#         self.new_win = Toplevel(self.root)
#         self.app = studentclass(self.new_win)

#     def add_result(self):
#         self.new_win = Toplevel(self.root)
#         self.app = ResultClass(self.new_win)

#     def add_viewresult(self):
#         self.new_win = Toplevel(self.root)
#         self.app = open_results_window(self.new_win)


# # MAIN
# if __name__ == "__main__":
#     root = Tk()
#     obj = NAME(root)
#     root.mainloop()


