import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

class EmployeeWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Employee Management")
        self.win.geometry("600x400")

        tk.Label(self.win, text="Name:").grid(row=0, column=0, pady=5)
        self.name_entry = tk.Entry(self.win)
        self.name_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.win, text="Department:").grid(row=1, column=0, pady=5)
        self.dept_entry = tk.Entry(self.win)
        self.dept_entry.grid(row=1, column=1, pady=5)

        tk.Button(self.win, text="Add Employee", command=self.add_employee).grid(row=2, column=0, pady=10)
        tk.Button(self.win, text="Delete Employee", command=self.delete_employee).grid(row=2, column=1, pady=10)

    def add_employee(self):
        name = self.name_entry.get()
        dept = self.dept_entry.get()
        if name.strip() == "" or dept.strip() == "":
            messagebox.showerror("Error", "Please fill all fields")
            return
        cursor.execute("INSERT INTO employees(name,dept) VALUES(?,?)", (name, dept))
        conn.commit()
        messagebox.showinfo("Success", "Employee added successfully")

    def delete_employee(self):
        name = self.name_entry.get()
        if name.strip() == "":
            messagebox.showerror("Error", "Please enter the employee name to delete")
            return
        cursor.execute("DELETE FROM employees WHERE name=?", (name,))
        conn.commit()
        messagebox.showinfo("Success", "Employee deleted successfully")

