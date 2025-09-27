import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

class AppointmentWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Appointment Management")
        self.win.geometry("600x400")

        tk.Label(self.win, text="Patient Name:").grid(row=0,column=0,pady=5)
        self.patient_entry = tk.Entry(self.win)
        self.patient_entry.grid(row=0,column=1,pady=5)

        tk.Label(self.win, text="Doctor Name:").grid(row=1,column=0,pady=5)
        self.doctor_entry = tk.Entry(self.win)
        self.doctor_entry.grid(row=1,column=1,pady=5)

        tk.Label(self.win, text="Date (YYYY-MM-DD):").grid(row=2,column=0,pady=5)
        self.date_entry = tk.Entry(self.win)
        self.date_entry.grid(row=2,column=1,pady=5)

        tk.Label(self.win, text="Time (HH:MM):").grid(row=3,column=0,pady=5)
        self.time_entry = tk.Entry(self.win)
        self.time_entry.grid(row=3,column=1,pady=5)

        tk.Button(self.win, text="Add Appointment", command=self.add_appointment).grid(row=4,column=0,pady=10)
        tk.Button(self.win, text="Delete Appointment", command=self.delete_appointment).grid(row=4,column=1,pady=10)

    def validate_date(self,date):
        return re.match(r"\d{4}-\d{2}-\d{2}$", date)

    def add_appointment(self):
        patient = self.patient_entry.get()
        doctor = self.doctor_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        if not patient or not doctor or not date or not time:
            messagebox.showerror("Error","Please fill all fields")
            return
        if not self.validate_date(date):
            messagebox.showerror("Error","Invalid date format")
            return
        cursor.execute("INSERT INTO appointments(patient_name,doctor_name,date,time) VALUES(?,?,?,?)",
                       (patient,doctor,date,time))
        conn.commit()
        messagebox.showinfo("Success","Appointment added successfully")

    def delete_appointment(self):
        patient = self.patient_entry.get()
        date = self.date_entry.get()
        if not patient or not date:
            messagebox.showerror("Error","Enter patient name and date to delete")
            return
        cursor.execute("DELETE FROM appointments WHERE patient_name=? AND date=?", (patient,date))
        conn.commit()
        messagebox.showinfo("Success","Appointment deleted successfully")



  
               
