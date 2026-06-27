import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def collect_dataset():

    student_name = name_entry.get().strip()

    if student_name == "":

        messagebox.showerror(
            "Error",
            "Enter Student Name"
        )

        return

    subprocess.run(
        [
            "python",
            "capture_smart.py",
            student_name
        ]
    )

def train_model():

    subprocess.run(
        ["python", "train_multiple.py"]
    )

    messagebox.showinfo(
        "Success",
        "Training Completed"
    )

def start_attendance():

    subprocess.run(
        ["python", "smart_attendance.py"]
    )

def view_attendance():

    if not os.path.exists(
        "attendance.csv"
    ):

        messagebox.showerror(
            "Error",
            "attendance.csv not found"
        )

        return

    window = tk.Toplevel()

    window.title(
        "Attendance Records"
    )

    window.geometry(
        "600x400"
    )

    text = tk.Text(
        window,
        font=("Consolas", 12)
    )

    text.pack(
        fill="both",
        expand=True
    )

    with open(
        "attendance.csv",
        "r"
    ) as file:

        data = file.read()

    text.insert(
        tk.END,
        data
    )

root = tk.Tk()

root.title(
    "Face Attendance System"
)

root.geometry(
    "400x400"
)

title = tk.Label(
    root,
    text="Face Attendance System",
    font=("Arial", 18, "bold")
)

name_label = tk.Label(
    root,
    text="Student Name"
)

name_label.pack()

name_entry = tk.Entry(
    root,
    width=30
)

name_entry.pack(pady=5)

btn1 = tk.Button(
    root,
    text="Collect Dataset",
    width=25,
    height=2,
    command=collect_dataset
)

btn1.pack(
    pady=10
)

btn2 = tk.Button(
    root,
    text="Train Model",
    width=25,
    height=2,
    command=train_model
)

btn2.pack(
    pady=10
)

btn3 = tk.Button(
    root,
    text="Start Attendance",
    width=25,
    height=2,
    command=start_attendance
)

btn3.pack(
    pady=10
)

btn4 = tk.Button(
    root,
    text="View Attendance",
    width=25,
    height=2,
    command=view_attendance
)

btn4.pack(
    pady=10
)

btn5 = tk.Button(
    root,
    text="Exit",
    width=25,
    height=2,
    command=root.destroy
)

btn5.pack(
    pady=10
)

root.mainloop()