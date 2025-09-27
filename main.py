import tkinter as tk
from patient import PatientWindow
from employee import EmployeeWindow
from room import RoomWindow
from appointment import AppointmentWindow
from billing import BillingWindow

class MainApp:
    def __init__(self, login_root):
        self.root = tk.Toplevel(login_root)
        self.root.title("Hospital Management System - Main")
        self.root.geometry("800x500")

        tk.Label(self.root, text="Hospital Management System", font=("Arial", 18, "bold")).pack(pady=20)

        tk.Button(self.root, text="Manage Patients", font=("Arial", 14), width=20, command=PatientWindow).pack(pady=5)
        tk.Button(self.root, text="Manage Employees", font=("Arial", 14), width=20, command=EmployeeWindow).pack(pady=5)
        tk.Button(self.root, text="Manage Rooms", font=("Arial", 14), width=20, command=RoomWindow).pack(pady=5)
        tk.Button(self.root, text="Appointments", font=("Arial", 14), width=20, command=AppointmentWindow).pack(pady=5)
        tk.Button(self.root, text="Billing", font=("Arial", 14), width=20, command=BillingWindow).pack(pady=5)
        tk.Button(self.root, text="Exit", font=("Arial", 14), width=20, command=self.root.destroy).pack(pady=20)
