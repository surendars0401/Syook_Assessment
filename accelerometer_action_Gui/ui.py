import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Syook assessment")


        self.tree = ttk.Treeview(self.root, columns=("Address", "X", "Y", "Z", "Status"), show="headings")
        self.tree.heading("Address", text="Device Address")
        self.tree.heading("X", text="X-axis (g)")
        self.tree.heading("Y", text="Y-axis (g)")
        self.tree.heading("Z", text="Z-axis (g)")
        self.tree.heading("Status", text="Status")
        self.tree.column("Address", width=150)
        self.tree.column("X", width=80)
        self.tree.column("Y", width=80)
        self.tree.column("Z", width=80)
        self.tree.column("Status", width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)


        self.devices = {}

    def update_device_list(self, address, x, y, z, status):

        if address in self.devices:
            self.tree.item(self.devices[address], values=(address, f"{x:.2f}", f"{y:.2f}", f"{z:.2f}", status))
        else:
            self.devices[address] = self.tree.insert("", tk.END,
                                                     values=(address, f"{x:.2f}", f"{y:.2f}", f"{z:.2f}", status))

    def run(self):
        self.root.mainloop()
