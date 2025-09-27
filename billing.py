import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

class BillingWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Billing Management")
        self.win.geometry("600x400")

        tk.Label(self.win, text="Patient Name:").grid(row=0,column=0,pady=5)
        self.patient_entry = tk.Entry(self.win)
        self.patient_entry.grid(row=0,column=1,pady=5)

        tk.Label(self.win, text="Amount:").grid(row=1,column=0,pady=5)
        self.amount_entry = tk.Entry(self.win)
        self.amount_entry.grid(row=1,column=1,pady=5)

        tk.Label(self.win, text="Date (YYYY-MM-DD):").grid(row=2,column=0,pady=5)
        self.date_entry = tk.Entry(self.win)
        self.date_entry.grid(row=2,column=1,pady=5)

        tk.Button(self.win, text="Add Bill", command=self.add_bill).grid(row=3,column=0,pady=10)
        tk.Button(self.win, text="Delete Bill", command=self.delete_bill).grid(row=3,column=1,pady=10)

    def validate_date(self,date):
        return re.match(r"\d{4}-\d{2}-\d{2}$", date)

    def add_bill(self):
        patient = self.patient_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()
        if not patient or not amount or not date:
            messagebox.showerror("Error","Please fill all fields")
            return
        if not self.validate_date(date):
            messagebox.showerror("Error","Invalid date format")
            return
        try:
            amount = float(amount)
        except:
            messagebox.showerror("Error","Invalid amount")
            return
        cursor.execute("INSERT INTO billing(patient_name,amount,date) VALUES(?,?,?)",
                       (patient,amount,date))
        conn.commit()
        messagebox.showinfo("Success","Bill added successfully")

    def delete_bill(self):
        patient = self.patient_entry.get()
        date = self.date_entry.get()
        if not patient or not date:
            messagebox.showerror("Error","Enter patient name and date to delete")
            return
        cursor.execute("DELETE FROM billing WHERE patient_name=? AND date=?", (patient,date))
        conn.commit()
        messagebox.showinfo("Success","Bill deleted successfully")


