import tkinter as tk
from tkinter import ttk, messagebox

import database
# Database
database.create_table()
# Main Window
root = tk.Tk()
root.title("Student Management System")
root.geometry("1200x650")
root.configure(bg="#dff3ff")
root.resizable(False, False)
# Variables
roll_var = tk.StringVar()
name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar(value="Male")
course_var = tk.StringVar()
mobile_var = tk.StringVar()
email_var = tk.StringVar()
search_var = tk.StringVar()
roll_var = tk.StringVar()
old_roll_no = None
# Functions
def clear_fields():
    roll_var.set("")
    name_var.set("")
    age_var.set("")
    gender_var.set("Male")
    course_var.set("")
    mobile_var.set("")
    email_var.set("")
    address_text.delete("1.0", tk.END)
    roll_entry.focus()
def get_form_data():
    roll = roll_var.get().strip()
    name = name_var.get().strip()
    age = age_var.get().strip()
    gender = gender_var.get().strip()
    course = course_var.get().strip()
    mobile = mobile_var.get().strip()
    email = email_var.get().strip()
    address = address_text.get("1.0", tk.END).strip()
    if not roll:
        messagebox.showerror("Error", "Please enter Roll No.")
        return None
    if not name:
        messagebox.showerror("Error", "Please enter Student Name.")
        return None
    if not age:
        messagebox.showerror("Error", "Please enter Age.")
        return None
    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be a number.")
        return None
    if age <= 0:
        messagebox.showerror("Error", "Please enter a valid age.")
        return None
    return (
        int(roll),name,age,gender,course,mobile,email,address
    )
def save_student():
    data = get_form_data()
    if data is None:
        return
    try:
        database.insert_student(data)
        messagebox.showinfo("Success", "Student record saved successfully."
        )
        show_all_students()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error",f"Unable to save student.\n\n{e}"
        )
def update_student():
    global old_roll_no
    data = get_form_data()
    if data is None:
        return
    if old_roll_no is None:
        messagebox.showerror( "Error","plz select a student from the table first."
        )
        return
    try:
        database.update_student(old_roll_no, data)
        messagebox.showinfo(
            "Success", "Student record updated successfully."
        )
        show_all_students()
        old_roll_no = None
    except Exception as e:
        messagebox.showerror(
            "Error", f"Unable to update student.\n\n{e}"
        )
def delete_student():
    roll = roll_var.get().strip()
    if not roll:
        messagebox.showerror("Error","Enter Roll No. to delete."
        )
        return
    result = messagebox.askyesno( "Confirm Delete", "Are you sure you want to delete this student?"
    )
    if result:
        try:
            database.delete_student(int(roll))
            messagebox.showinfo( "Success","Student record deleted successfully."
            )
            show_all_students()
            clear_fields()
        except Exception as e:
            messagebox.showerror("Error",f"Unable to delete student.\n\n{e}"
            )
def show_all_students():
    for item in student_table.get_children():
        student_table.delete(item)
    rows = database.get_students()
    for row in rows:
        student_table.insert("", tk.END, values=row)
def search_students():
    search_value = search_var.get().strip()
    for item in student_table.get_children():
        student_table.delete(item)
    if search_value == "":
        show_all_students()
        return
    try:
        rows = database.search_student(int(search_value))
        for row in rows:
            student_table.insert("", tk.END, values=row)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid Roll No."
        )
def select_student(event):
    global old_roll_no
    selected = student_table.focus()
    if not selected:
        return
    values = student_table.item(selected, "values")
    if not values:
        return
    old_roll_no = int(values[0])
    roll_var.set(values[0])
    name_var.set(values[1])
    age_var.set(values[2])
    gender_var.set(values[3])
    course_var.set(values[4])
    mobile_var.set(values[5])
    email_var.set(values[6])
    address_text.delete("1.0", tk.END)
    address_text.insert("1.0", values[7])
# Header
title = tk.Label(
    root,text="STUDENT MANAGEMENT SYSTEM",font=("Arial", 22, "bold"),bg="#0b2d4d",fg="white",pady=12
)
title.pack(fill=tk.X)
# Main Container
main_frame = tk.Frame(
    root,
    bg="#dff3ff"
)
main_frame.pack(
    fill=tk.BOTH,expand=True,padx=15,pady=15
)
# Left Frame - Student Information
left_frame = tk.LabelFrame(
    main_frame,text="Student Information",font=("Arial", 13, "bold"),bg="#dff3ff",fg="#12344d", padx=15, pady=15
)
left_frame.pack(
    side=tk.LEFT,fill=tk.Y,padx=(0, 10)
)
# Labels and Entries
label_font = ("Arial", 11, "bold")
tk.Label(
    left_frame,text="Roll No",font=label_font,bg="#dff3ff"
).grid(row=0, column=0, sticky="w", pady=7)
roll_entry = tk.Entry(
    left_frame,textvariable=roll_var,font=("Arial", 11),
    width=24
)
roll_entry.grid(row=0, column=1, pady=7)
tk.Label(
    left_frame,text="Name",font=label_font,bg="#dff3ff"
).grid(row=1, column=0, sticky="w", pady=7)
name_entry = tk.Entry(
    left_frame,textvariable=name_var,font=("Arial", 11), width=24
)
name_entry.grid(row=1, column=1, pady=7)
tk.Label(
    left_frame,text="Age",font=label_font,bg="#dff3ff"
).grid(row=2, column=0, sticky="w", pady=7)
age_entry = tk.Entry(
    left_frame, textvariable=age_var, font=("Arial", 11), width=24
)
age_entry.grid(row=2, column=1, pady=7)
tk.Label(
    left_frame, text="Gender", font=label_font, bg="#dff3ff"
).grid(row=3, column=0, sticky="w", pady=7)
gender_combo = ttk.Combobox(
    left_frame,textvariable=gender_var,values=["Male", "Female", "Other"],state="readonly",width=22
)
gender_combo.grid(row=3, column=1, pady=7)
tk.Label(
    left_frame,text="Course",font=label_font,bg="#dff3ff"
).grid(row=4, column=0, sticky="w", pady=7)
course_combo = ttk.Combobox( left_frame, textvariable=course_var,
    values=[
        "Python", "Java","C","C++","Web Development","AI","Data Science","BCA","MCA"],
    width=22
)
course_combo.grid(row=4, column=1, pady=7)
tk.Label(
    left_frame,text="Mobile",font=label_font,bg="#dff3ff"
).grid(row=5, column=0, sticky="w", pady=7)
mobile_entry = tk.Entry(left_frame,textvariable=mobile_var,font=("Arial", 11),width=24
)
mobile_entry.grid(row=5, column=1, pady=7)
tk.Label(left_frame,text="Email",font=label_font,bg="#dff3ff"
).grid(row=6, column=0, sticky="w", pady=7)
email_entry = tk.Entry(left_frame,textvariable=email_var,font=("Arial", 11),width=24
)
email_entry.grid(row=6, column=1, pady=7)
tk.Label(
    left_frame,text="Address",font=label_font,bg="#dff3ff"
).grid(row=7, column=0, sticky="nw", pady=7)
address_text = tk.Text(left_frame,width=24,height=4,font=("Arial", 11)
)
address_text.grid(row=7, column=1, pady=7)
# Buttons
button_frame = tk.Frame( left_frame, bg="#dff3ff"
)
button_frame.grid(row=8,column=0,columnspan=2,pady=15
)
save_button = tk.Button( button_frame, text="Save", command=save_student, bg="#198754",fg="white", font=("Arial", 10, "bold"), width=8
)
save_button.grid(row=0, column=0, padx=3)
update_button = tk.Button( button_frame,text="Update",command=update_student,bg="#0d6efd",fg="white",font=("Arial", 10, "bold"),width=8
)
update_button.grid(row=0, column=1, padx=3)
delete_button = tk.Button(button_frame,text="Delete",command=delete_student,bg="#35dcc6",fg="white",font=("Arial", 10, "bold"),width=8
)
delete_button.grid(row=0, column=2, padx=3)
clear_button = tk.Button(button_frame,text="Clear",command=clear_fields,bg="#ffc107",fg="black",font=("Arial", 10, "bold"),width=8
)
clear_button.grid(row=0, column=3, padx=3)
# Right Frame - Student Records
right_frame = tk.LabelFrame(main_frame,text="Student Records",font=("Arial", 13, "bold"),bg="#f2dfff",fg="#124d2d",padx=10,pady=10
)
right_frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=True
)
# Search Area
search_frame = tk.Frame(right_frame, bg="#ffdfef"
)
search_frame.pack(fill=tk.X,pady=(0, 10)
)
tk.Label(search_frame,text="Search Roll No:",font=("Arial", 10, "bold"),bg="#4ba5dd"
).pack(side=tk.LEFT, padx=5)
search_entry = tk.Entry(search_frame,textvariable=search_var,font=("Arial", 10),width=18
)
search_entry.pack(side=tk.LEFT, padx=5)
search_button = tk.Button(search_frame,text="Search",command=search_students,bg="#580fdf",fg="white",font=("Arial", 10, "bold")
)
search_button.pack(side=tk.LEFT, padx=5)
show_button = tk.Button(search_frame,text="Show All",command=show_all_students,bg="#873419",fg="white",font=("Arial", 10, "bold")
)
show_button.pack(side=tk.LEFT, padx=5)
# Student Table
table_frame = tk.Frame( right_frame, bg="white"
)

table_frame.pack( fill=tk.BOTH,expand=True
)
columns = ( "Roll No", "Name", "Age", "Gender", "Course", "Mobile", "Email", "Address"
)
student_table = ttk.Treeview(table_frame,columns=columns,show="headings",height=20
)
column_widths = {
    "Roll No": 70,"Name": 120,"Age": 50,"Gender": 80,"Course": 120,"Mobile": 110,"Email": 160,"Address": 160
}
for column in columns:
    student_table.heading( column, text=column
    )
    student_table.column(column,width=column_widths[column], anchor="center"
    )
vertical_scrollbar = ttk.Scrollbar(table_frame,orient=tk.VERTICAL,command=student_table.yview
)
horizontal_scrollbar = ttk.Scrollbar(table_frame,orient=tk.HORIZONTAL,command=student_table.xview
)
student_table.configure(yscrollcommand=vertical_scrollbar.set,xscrollcommand=horizontal_scrollbar.set
)
student_table.grid( row=0,column=0,sticky="nsew"
)
vertical_scrollbar.grid(row=0,column=1,sticky="ns"
)
horizontal_scrollbar.grid(row=1,column=0,sticky="ew"
)
table_frame.grid_rowconfigure( 0, weight=1
)
table_frame.grid_columnconfigure( 0, weight=1
)
student_table.bind(
    "<ButtonRelease-1>",select_student
)
# Initial Data
show_all_students()
roll_entry.focus
# Run Application
root.mainloop()