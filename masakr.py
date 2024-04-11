import tkinter as tk  # importuje knihovnu tkinter jako tk
from tkinter import messagebox  # z knihovny tkinter importuje messagebox

class PointSortingApp:  # definuje tridu PointSortingApp
    def __init__(self, master):  # definuje metodu __init__ s parametrem master
        self.master = master  # nastavi master na self.master
        self.master.title("Radici masakr")  # nastavi titulek okna
        
        self.points = []  # vytvori prazdnej seznam bodu
        
        # souradnice vstup pole
        self.x_entry = tk.Entry(master, width=5)  # vytvori vstupni pole pro x souradnici
        self.x_entry.grid(row=0, column=0, padx=5, pady=5)  # da vstupni pole na prvni radek a prvni sloupec
        self.y_entry = tk.Entry(master, width=5)  # vytvori vstupni pole pro y souradnici
        self.y_entry.grid(row=0, column=1, padx=5, pady=5)  # da vstupni pole na prvni rdek a druhej sloupec

        # ref souradnice vstup pole
        self.ref_x_entry = tk.Entry(master, width=5)  # vytvori vstupni pole pro referencni x souradnici
        self.ref_x_entry.grid(row=1, column=0, padx=5, pady=5)  # da vstupni pole na druhej radek a prvni sloupec
        self.ref_y_entry = tk.Entry(master, width=5)  # vytvori vstupni pole pro referencni y souradnici
        self.ref_y_entry.grid(row=1, column=1, padx=5, pady=5)  # da vstupni pole na druhej radek a druhej sloupec

        # seznam pole
        self.points_listbox = tk.Listbox(master, width=40)  # vytvori listbox pro zobrazeni bodu
        self.points_listbox.grid(row=2, column=0, columnspan=4, padx=5, pady=5)  # da listbox na treti radek a roztahne pres ctyri sloupce

        # pridavaci cudlik
        self.add_button = tk.Button(master, text="PRIDAT BOD", command=self.add_point)  # vytvori cudlik pro pridani bodu
        self.add_button.grid(row=0, column=2, padx=5, pady=5)  # da cudlik na prvni radek a treti sloupec

        # mazaci cudlik
        self.delete_button = tk.Button(master, text="SMAZAT", command=self.delete_point)  # vytvori cudlik pro smazani bodu
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)  # da cudlik na prvni radek a ctvrtej sloupec

        # radici cudlik
        self.sort_button = tk.Button(master, text="SERADIT BODY", command=self.sort_points)  # vytvori cudlik pro serazeni bodu
        self.sort_button.grid(row=1, column=2, columnspan=2, padx=5, pady=5)  # da cudlik na druhej radek a roztahne pres dva sloupce

    # pridat nast
    def add_point(self):  # definuje metodu add_point
        x = self.x_entry.get()  # ziska hodnotu z x_entry
        y = self.y_entry.get()  # ziska hodnotu z y_entry
        if x and y:  # pokud x a y existujou
            name = chr(ord('a') + len(self.points))  # vytvori nazev bodu jako pismeno abecedy
            self.points.append((float(x), float(y), name))  # prida novej bod do seznamu bodu
            self.points_listbox.insert(tk.END, f"{name} ({x}, {y})")  # vlozi novej bod do listboxu

    # smazat nast
    def delete_point(self):  # definuje metodu delete_point
        selection = self.points_listbox.curselection()  # ziska vybranej bod v listboxu
        if selection:  # pokud je neco vybrany
            index = selection[0]  # ziska index vybranyho bodu
            self.points_listbox.delete(index)  # smaze bod z listboxu
            del self.points[index]  # smaze bod ze seznamu bodu

    # razeni nast
    def sort_points(self):  # definuje metodu sort_points
        ref_x = float(self.ref_x_entry.get())  # ziska referencni x souradnici
        ref_y = float(self.ref_y_entry.get())  # ziska referencni y souradnici
        sorted_points = sorted(self.points, key=lambda point: (point[0] - ref_x)**2 + (point[1] - ref_y)**2)  # seradi body podle vzdalenosti od referencniho bodu
        result = "Body serazene podle blizkosti k referencnim souradnicim:\n\n"  # vytvori vyslednej retezec
        sorted_result = []  # inicializuje seznam pro serazeny body
        prev_distance = None  # inicializuje promennou (lol) pro predchozi vzdalenost
        for point in sorted_points:  # pro kazdej bod v serazenych bodech
            distance = (point[0] - ref_x)**2 + (point[1] - ref_y)**2  # spocita vzdalenost bodu od referencniho
            if prev_distance is not None and distance == prev_distance:  # pokud je vzdalenost stejna jako predchozi
                sorted_result[-1] += f"; {point[2]} ({point[0]}, {point[1]})"  # prida bod k predchozumu bodu
            else:  # jinak
                sorted_result.append(f"{point[2]} ({point[0]}, {point[1]})")  # prida novej bod do seznamu
            prev_distance = distance  # nastavi predchozi vzdalenost na aktualni vzdalenost
        result += "\n".join(sorted_result)  # spojuje body serazeny podle vzdalenosti s odradkovanim
        messagebox.showinfo("Serazene body", result)  # zobrazi dialog okno se serazenejma bodama

def main():  # definuje funkci main
    root = tk.Tk()  # vytvori hlavni okno
    app = PointSortingApp(root)  # vytvori instanci aplikace
    root.mainloop()  # spusti hlavni smycku

if __name__ == "__main__":  # pokud je tenhle skript spustenej prrimo
    main()  # spusto funkci main
