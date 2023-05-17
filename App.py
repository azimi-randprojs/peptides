import tkinter as tk
from tkinter import messagebox, CENTER, E, W

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.generate_app()

    def generate_app(self):
        self.master.geometry("800x800")
        self.master.title("DNA Sequence Reader")
        self.master.configure(background="white")

        self.empty_frame_one = tk.Frame(height=300, background="white")
        self.empty_frame_one.pack()

        self.title = tk.Label(self.master, text="DNA Sequence Reader", font="Helvetica 18 bold", fg="darkgreen", bg="white")
        self.title.configure(anchor=CENTER)
        self.title.pack()

        self.empty_frame_two = tk.Frame(height=20, background="white")
        self.empty_frame_two.pack()

        self.directions = tk.Label(self.master, text="Input a DNA sequence below (5' - 3'):", font="Helvetica 12", fg="black", bg="white", height=2)
        self.directions.configure(anchor=CENTER)
        self.directions.pack()

        self.entry_frame = tk.Frame(background="white")
        self.entry = tk.Entry(self.entry_frame, font="Helvetica 12", bd="4", fg="black", bg="white")
        self.entry.grid(row=0, sticky=E+W)

        self.entryScroll = tk.Scrollbar(self.entry_frame, orient=tk.HORIZONTAL, command=self.__scrollHandler)
        self.entryScroll.grid(row=1, sticky=E+W)
        self.entry['xscrollcommand'] = self.entryScroll.set
        self.entry_frame.pack()

        self.button_frame = tk.Frame(background="white")
        self.find_complement_btn = tk.Button(self.button_frame, text="Find Complement\n(5' - 3')", width=11, height=2)
        self.find_peptide_seq_btn = tk.Button(self.button_frame, text="Find Corresponding\nPeptide Sequence", width=11, height=2)
        self.find_complement_btn.grid(row =0, column=0, padx=10)
        self.find_peptide_seq_btn.grid(row = 0, column=1, padx=10)
        self.button_frame.pack()

    def __scrollHandler(self, *L):
        op, howMany = L[0], L[1]

        if op == 'scroll':
            units = L[2]
            self.entry.xview_scroll(howMany, units)
        elif op == 'moveto':
            self.entry.xview_moveto(howMany)

def on_closing(): 
    """Function to confirm with user whether they want to quit the app.
    Works with tkinter message box
    """
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy() #Destroy root window (i.e destroy application)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root) #Create GUI app loop
    app.pack(fill="both", expand=True)
    app.configure(background="white")
    root.protocol("WM_DELETE_WINDOW", on_closing) #Check with user whether they want to close or not
    root.configure()
    root.mainloop() #GUI main loop