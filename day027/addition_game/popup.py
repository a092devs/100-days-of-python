import tkinter

FONT = ("Consolas", 16, "normal")

class Popup(tkinter.Tk):
    def __init__(self, title, text):
        super().__init__()
        self.title(title)
        self.config(padx=10, pady=10)
        self.generate_text(text)
        self.generate_button()
        self.bind_all("<Any-KeyPress>", self.keypress_handler)
        self.protocol("WM_DELETE_WINDOW", self.exit_window)
        self.focus_force()

    def generate_text(self, text):
        self.label = tkinter.Label(self, text=text, font=FONT)
        self.label.grid(column=0, row=0, columnspan=2)

    def generate_button(self):
        self.button = tkinter.Button(self, text="OK", font=FONT, command=self.exit_window)
        self.button.grid(column=1, row=1)

    def keypress_handler(self, event):
        if event.keysym in ["Return", "Escape"]:
            self.exit_window()

    def exit_window(self):
        self.destroy()