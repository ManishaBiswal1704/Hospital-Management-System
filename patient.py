import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

class PatientWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Patient Management")
        self.win.geometry("700x500")

        tk.Label(self.win, text="Name:").grid(row=0, column=0, pady=5)
        self.name_entry = tk.Entry(self.win)
        self.name_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.win, text="Age:").grid(row=1, column=0, pady=5)
        self.age_entry = tk.Entry(self.win)
        self.age_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.win, text="Sex:").grid(row=2, column=0, pady=5)
        self.sex_entry = tk.Entry(self.win)
        self.sex_entry.grid(row=2, column=1, pady=5)

        tk.Label(self.win, text="Phone:").grid(row=3, column=0, pady=5)
        self.phone_entry = tk.Entry(self.win)
        self.phone_entry.grid(row=3, column=1, pady=5)

        tk.Label(self.win, text="Address:").grid(row=4, column=0, pady=5)
        self.address_entry = tk.Entry(self.win)
        self.address_entry.grid(row=4, column=1, pady=5)

        tk.Label(self.win, text="Disease:").grid(row=5, column=0, pady=5)
        self.disease_entry = tk.Entry(self.win)
        self.disease_entry.grid(row=5, column=1, pady=5)

        tk.Label(self.win, text="Appointment (YYYY-MM-DD):").grid(row=6, column=0, pady=5)
        self.appointment_entry = tk.Entry(self.win)
        self.appointment_entry.grid(row=6, column=1, pady=5)

        tk.Label(self.win, text="Room No:").grid(row=7, column=0, pady=5)
        self.room_entry = tk.Entry(self.win)
        self.room_entry.grid(row=7, column=1, pady=5)

        tk.Label(self.win, text="Admission Date (YYYY-MM-DD):").grid(row=8, column=0, pady=5)
        self.admission_entry = tk.Entry(self.win)
        self.admission_entry.grid(row=8, column=1, pady=5)

        tk.Label(self.win, text="Discharge Date (YYYY-MM-DD):").grid(row=9, column=0, pady=5)
        self.discharge_entry = tk.Entry(self.win)
        self.discharge_entry.grid(row=9, column=1, pady=5)

        tk.Button(self.win, text="Add Patient", command=self.add_patient).grid(row=10, column=0, pady=10)
        tk.Button(self.win, text="Delete Patient", command=self.delete_patient).grid(row=10, column=1, pady=10)

    def validate_date(self, date):
        return re.match(r"\d{4}-\d{2}-\d{2}$", date)

    def validate_phone(self, phone):
        return re.match(r"^\d{10}$", phone)

    def add_patient(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        sex = self.sex_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        disease = self.disease_entry.get()
        appointment = self.appointment_entry.get()
        room = self.room_entry.get()
        admission = self.admission_entry.get()
        discharge = self.discharge_entry.get()

        if not self.validate_phone(phone):
            messagebox.showerror("Error","Invalid phone number")
            return
        if appointment and not self.validate_date(appointment):
            messagebox.showerror("Error","Invalid appointment date")
            return
        if admission and not self.validate_date(admission):
            messagebox.showerror("Error","Invalid admission date")
            return
        if discharge and not self.validate_date(discharge):
            messagebox.showerror("Error","Invalid discharge date")
            return

        cursor.execute("""INSERT INTO patients(name,age,sex,phone,address,disease,appointment,room_no,admission_date,discharge_date)
                        VALUES(?,?,?,?,?,?,?,?,?,?)""",
                       (name,age,sex,phone,address,disease,appointment,room,admission,discharge))
        conn.commit()
        messagebox.showinfo("Success","Patient added successfully")

    def delete_patient(self):
        name = self.name_entry.get()
        cursor.execute("DELETE FROM patients WHERE name=?", (name,))
        conn.commit()
        messagebox.showinfo("Success","Patient deleted successfully")
