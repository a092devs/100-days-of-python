from tkinter import *
import requests

FONT_SIZES=[(150,15), (120,18), (90,21), (70,24), (50,27), (30,30), (20,33), (12,36), (1,39)]

def fit_font(n_chars):
    for (chars, font_size) in FONT_SIZES:
        if n_chars > chars:
            return font_size

def get_quote():
    res = requests.get('https://api.britney.rest').json()
    font_size = fit_font(len(res))
    canvas.itemconfigure( quote_text, text=res, font=("Arial", font_size, 'bold'))

window = Tk()
window.title("Britney Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Britney Speaks", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

britney_img = PhotoImage(file="britney.png")
britney_button = Button(image=britney_img, highlightthickness=0, command=get_quote)
britney_button.grid(row=1, column=0)

window.mainloop()