import tkinter as tk
from tkinter import messagebox
import sqlite3
from main import MainApp  # Import main menu

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user,pwd))
    if cursor.fetchone():
        messagebox.showinfo("Success", f"Welcome {user}!")
        root.withdraw()  # Hide login
        MainApp(root)    # Open main menu
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Login window
root = tk.Tk()
root.title("Login")
root.geometry("600x400")
root.resizable(True, True)

tk.Label(root, text="Hospital Management System", font=("Arial", 20, "bold")).pack(pady=30)
tk.Label(root, text="Username:", font=("Arial", 14)).pack(pady=5)
username_entry = tk.Entry(root, font=("Arial", 14))
username_entry.pack(pady=5)
tk.Label(root, text="Password:", font=("Arial", 14)).pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 14), show="*")
password_entry.pack(pady=5)
tk.Button(root, text="Login", font=("Arial", 14), width=10, command=login).pack(pady=20)

root.mainloop()



















