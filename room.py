import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

class RoomWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Room Management")
        self.win.geometry("600x400")

        tk.Label(self.win, text="Room No:").grid(row=0, column=0, pady=5)
        self.room_entry = tk.Entry(self.win)
        self.room_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.win, text="Type:").grid(row=1, column=0, pady=5)
        self.type_entry = tk.Entry(self.win)
        self.type_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.win, text="Status:").grid(row=2, column=0, pady=5)
        self.status_entry = tk.Entry(self.win)
        self.status_entry.grid(row=2, column=1, pady=5)

        tk.Button(self.win, text="Add Room", command=self.add_room).grid(row=3, column=0, pady=10)
        tk.Button(self.win, text="Delete Room", command=self.delete_room).grid(row=3, column=1, pady=10)

    def add_room(self):
        room = self.room_entry.get()
        rtype = self.type_entry.get()
        status = self.status_entry.get()
        if room.strip() == "" or rtype.strip() == "" or status.strip() == "":
            messagebox.showerror("Error", "Please fill all fields")
            return
        cursor.execute("INSERT INTO rooms(room_no,type,status) VALUES(?,?,?)", (room,rtype,status))
        conn.commit()
        messagebox.showinfo("Success","Room added successfully")

    def delete_room(self):
        room = self.room_entry.get()
        if room.strip() == "":
            messagebox.showerror("Error", "Please enter room number")
            return
        cursor.execute("DELETE FROM rooms WHERE room_no=?", (room,))
        conn.commit()
        messagebox.showinfo("Success","Room deleted successfully")


