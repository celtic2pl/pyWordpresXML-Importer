import tkinter as tk

# Console
print('Hello World!')


top = tk.Tk()
B = tk.Button(top, text="Hello World!")
B.pack()
top.mainloop()


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.hi_there = None

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World!"
        self.hi_there.pack(side="top")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

