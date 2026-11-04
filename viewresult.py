
from tkinter import *
from tkinter import ttk, messagebox
import csv, os

def open_results_window(win):
    win.title("View Student Results")
    win.geometry("900x650+250+100")
    win.config(bg="white")

    Label(win, text="Student Results Viewer", font=("goudy old style", 20, "bold"),
          bg="#00BCD4", fg="white").pack(fill=X)

    # ---------- Search Bar ----------
    Label(win, text="Search Roll No / Name:", font=("goudy old style", 13, "bold"),
          bg="white").place(x=20, y=65)
    search_var = StringVar()
    search_entry = Entry(win, textvariable=search_var, font=("goudy old style", 13),
                         bg="#f2f2f2")
    search_entry.place(x=220, y=65, width=200, height=30)

    # ---------- File List ----------
    frame = Frame(win, bd=2, relief=RIDGE, bg="white")
    frame.place(x=20, y=110, width=250, height=450)

    Label(frame, text="Saved Result Files", font=("goudy old style", 14, "bold"),
          bg="white").pack(anchor=W, padx=10, pady=5)

    file_list = Listbox(frame, font=("goudy old style", 13), bg="#F3F3F3")
    file_list.pack(fill=BOTH, expand=1, padx=10, pady=5)

    # ---------- Table ----------
    table_frame = Frame(win, bg="white", bd=2, relief=RIDGE)
    table_frame.place(x=300, y=150, width=570, height=380)

    table = ttk.Treeview(table_frame, columns=("subject", "marks_obtained", "full_marks"),
                         show="headings")
    table.heading("subject", text="Subject")
    table.heading("marks_obtained", text="Obtained")
    table.heading("full_marks", text="Full Marks")
    table.pack(fill=BOTH, expand=1)

    lbl_info = Label(win, text="", bg="white", font=("goudy old style", 14))
    lbl_info.place(x=300, y=110)

    lbl_total = Label(win, text="", bg="white",
                      font=("goudy old style", 14, "bold"), fg="green")
    lbl_total.place(x=300, y=540)

    # ---------- Functions ----------
    def load_files():
        file_list.delete(0, END)
        if not os.path.exists("data"):
            os.makedirs("data")
        for file in os.listdir("data"):
            if file.endswith(".csv"):
                file_list.insert(END, file)

    def show_selected_file(event=None):
        selected = file_list.curselection()
        if not selected:
            return

        file_name = file_list.get(selected[0])
        file_path = os.path.join("data", file_name)

        try:
            with open(file_path, "r") as f:
                reader = csv.reader(f)
                rows = list(reader)

            lbl_info.config(text=f"Showing: {file_name}")
            table.delete(*table.get_children())

            total_obt = 0
            total_full = 0
            start = 0

            for i, row in enumerate(rows):
                if row and row[0] == "Subject":
                    start = i + 1
                    break

            for row in rows[start:]:
                if len(row) == 3 and row[0] != "Total Obtained":
                    table.insert("", END, values=row)
                    try:
                        total_obt += float(row[1])
                        total_full += float(row[2])
                    except:
                        pass

                elif len(row) >= 3 and row[0] == "Total Obtained":
                    total_obt = row[1]
                    total_full = row[2]

            lbl_total.config(text=f"Total Marks: {total_obt} / {total_full}")

        except Exception as e:
            messagebox.showerror("Error", f"Unable to load file!\n{e}")

    def search_files():
        query = search_var.get().strip().lower()
        file_list.delete(0, END)
        for file in os.listdir("data"):
            if file.endswith(".csv") and (query in file.lower() or not query):
                file_list.insert(END, file)

    def delete_selected_file():
        selected = file_list.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a file to delete!")
            return

        file_name = file_list.get(selected[0])
        file_path = os.path.join("data", file_name)

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete:\n{file_name} ?"
        )

        if confirm:
            try:
                os.remove(file_path)
                messagebox.showinfo("Success", "File deleted successfully!")
                file_list.delete(selected[0])
                table.delete(*table.get_children())
                lbl_info.config(text="")
                lbl_total.config(text="")
            except Exception as e:
                messagebox.showerror("Error", f"Unable to delete file!\n{e}")

    # ---------- Buttons ----------
    Button(win, text="Reload List", font=("goudy old style", 13, "bold"),
           bg="#4CAF50", fg="white",
           command=load_files).place(x=660, y=65, width=100, height=30)

    Button(win, text="Delete File", font=("goudy old style", 13, "bold"),
           bg="#F44336", fg="white",
           command=delete_selected_file).place(x=530, y=65, width=100, height=30)

    Button(win, text="Search", font=("goudy old style", 12, "bold"),
           bg="#2196F3", fg="white",
           command=search_files).place(x=420, y=65, width=80, height=30)

    file_list.bind("<<ListboxSelect>>", show_selected_file)

    load_files()

# ---------- Run App ----------
if __name__ == "__main__":
    root = Tk()
    open_results_window(root)
    root.mainloop()
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
  # from tkinter import *
# from tkinter import ttk, messagebox
# import csv, os

# def open_results_window(win):
#     win.title("View Student Results")
#     win.geometry("900x650+250+100")
#     win.config(bg="white")

#     Label(win, text="Student Results Viewer", font=("goudy old style", 20, "bold"),
#           bg="#00BCD4", fg="white").pack(fill=X)

#     # ---------- File List ----------
#     frame = Frame(win, bd=2, relief=RIDGE, bg="white")
#     frame.place(x=20, y=110, width=250, height=450)

#     Label(frame, text="Saved Result Files", font=("goudy old style", 14, "bold"),
#           bg="white").pack(anchor=W, padx=10, pady=5)

#     file_list = Listbox(frame, font=("goudy old style", 13), bg="#F3F3F3")
#     file_list.pack(fill=BOTH, expand=1, padx=10, pady=5)

#     # ---------- Search Bar ----------
#     Label(win, text="Search Roll No / Name:", font=("goudy old style", 13, "bold"),
#           bg="white").place(x=20, y=65)
#     search_var = StringVar()
#     search_entry = Entry(win, textvariable=search_var, font=("goudy old style", 13),
#                          bg="#f2f2f2")
#     search_entry.place(x=220, y=65, width=200, height=30)

#     # ---------- Table ----------
#     table_frame = Frame(win, bg="white", bd=2, relief=RIDGE)
#     table_frame.place(x=300, y=150, width=570, height=380)

#     table = ttk.Treeview(table_frame, columns=("subject", "marks_obtained", "full_marks"),
#                          show="headings")
#     table.heading("subject", text="Subject")
#     table.heading("marks_obtained", text="Obtained")
#     table.heading("full_marks", text="Full Marks")
#     table.pack(fill=BOTH, expand=1)

#     lbl_info = Label(win, text="", bg="white", font=("goudy old style", 14))
#     lbl_info.place(x=300, y=110)

#     lbl_total = Label(win, text="", bg="white",
#                       font=("goudy old style", 14, "bold"), fg="green")
#     lbl_total.place(x=300, y=540)

#     # ---------- Functions ----------
#     def load_files():
#         file_list.delete(0, END)
#         if not os.path.exists("data"):
#             os.makedirs("data")
#         for file in os.listdir("data"):
#             if file.endswith(".csv"):
#                 file_list.insert(END, file)

#     def show_selected_file(event=None):
#         selected = file_list.curselection()
#         if not selected:
#             return
#         file_name = file_list.get(selected[0])
#         file_path = os.path.join("data", file_name)
#         try:
#             with open(file_path, "r") as f:
#                 reader = csv.reader(f)
#                 rows = list(reader)
#             lbl_info.config(text=f"Showing: {file_name}")
#             table.delete(*table.get_children())

#             start = 0
#             total_obt = 0
#             total_full = 0
#             for i, row in enumerate(rows):
#                 if row and row[0] == "Subject":
#                     start = i + 1
#                     break

#             for row in rows[start:]:
#                 if len(row) == 3 and row[0] != "Total Obtained":
#                     try:
#                         obt = float(row[1])
#                         full = float(row[2])
#                         total_obt += obt
#                         total_full += full
#                     except:
#                         pass
#                     table.insert("", END, values=row)
#                 elif len(row) >= 2 and row[0] == "Total Obtained":
#                     try:
#                         total_obt = float(row[1])
#                         total_full = float(row[2])
#                     except:
#                         pass

#             lbl_total.config(text=f"Total Marks: {total_obt} / {total_full}")

#         except Exception as e:
#             messagebox.showerror("Error", f"Unable to load file!\n{e}")

#     def search_files():
#         query = search_var.get().strip().lower()
#         file_list.delete(0, END)
#         for file in os.listdir("data"):
#             if file.endswith(".csv") and (query in file.lower() or not query):
#                 file_list.insert(END, file)

#     file_list.bind("<<ListboxSelect>>", show_selected_file)

#     Button(win, text="Reload List", font=("goudy old style", 13, "bold"),
#            bg="#4CAF50", fg="white", command=load_files).place(x=50, y=20, width=180, height=30)

#     Button(win, text="Search", font=("goudy old style", 12, "bold"),
#            bg="#2196F3", fg="white", command=search_files).place(x=430, y=65, width=80, height=30)

#     load_files()

# # ---------- Run the app ----------
# if __name__ == "__main__":
#     root = Tk()
#     open_results_window(root)
#     root.mainloop()

