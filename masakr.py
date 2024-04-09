import tkinter as tk
from tkinter import messagebox

class PointSortingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Řadící masakr")
        
        self.points = []
        
        # souradnice vstup pole
        self.x_entry = tk.Entry(master, width=5)
        self.x_entry.grid(row=0, column=0, padx=5, pady=5)
        self.y_entry = tk.Entry(master, width=5)
        self.y_entry.grid(row=0, column=1, padx=5, pady=5)

        # ref souradnice vstup pole
        self.ref_x_entry = tk.Entry(master, width=5)
        self.ref_x_entry.grid(row=1, column=0, padx=5, pady=5)
        self.ref_y_entry = tk.Entry(master, width=5)
        self.ref_y_entry.grid(row=1, column=1, padx=5, pady=5)

        # seznam pole
        self.points_listbox = tk.Listbox(master, width=40)
        self.points_listbox.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        # pridat cudlik
        self.add_button = tk.Button(master, text="PŘIDAT BOD", command=self.add_point)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        # smazat cudlik
        self.delete_button = tk.Button(master, text="SMAZAT", command=self.delete_point)
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)

        # seradit cudlik
        self.sort_button = tk.Button(master, text="SEŘADIT BODY", command=self.sort_points)
        self.sort_button.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

    # pridat nast
    def add_point(self):
        x = self.x_entry.get()
        y = self.y_entry.get()
        if x and y:
            name = chr(ord('A') + len(self.points))  # abeceda
            self.points.append((float(x), float(y), name))
            self.points_listbox.insert(tk.END, f"{name} ({x}, {y})")

    # smazat nast
    def delete_point(self):
        selection = self.points_listbox.curselection()
        if selection:
            index = selection[0]
            self.points_listbox.delete(index)
            del self.points[index]

    # razeni nast
    def sort_points(self):
        ref_x = float(self.ref_x_entry.get())
        ref_y = float(self.ref_y_entry.get())
        sorted_points = sorted(self.points, key=lambda point: (point[0] - ref_x)**2 + (point[1] - ref_y)**2)
        result = "Body seřazené podle blízkosti k referenčním souřadnicím:\n\n"
        sorted_result = []
        prev_distance = None
        for point in sorted_points:
            distance = (point[0] - ref_x)**2 + (point[1] - ref_y)**2
            if prev_distance is not None and distance == prev_distance:
                sorted_result[-1] += f"; {point[2]} ({point[0]}, {point[1]})"
            else:
                sorted_result.append(f"{point[2]} ({point[0]}, {point[1]})")
            prev_distance = distance
        result += "\n".join(sorted_result)
        messagebox.showinfo("Seřazené body", result)

def main():
    root = tk.Tk()
    app = PointSortingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()