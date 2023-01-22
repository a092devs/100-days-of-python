from tkinter import *

def convert(*args):
    while True:
        try:
            user_input = float(my_input1.get())
        except ValueError:
            break
        else:
            if tkvar1.get() == tkvar2.get():
                result = user_input
            elif tkvar1.get() == 'Fahrenheit':
                result = (user_input - 32) * 5 / 9
            else:
                result = (user_input * 9 / 5) + 32
            result_label.config(text=round(result, 2))
            break

window = Tk()
window.minsize(width=300, height=200)
window.title('Temperature Converter')

my_input1 = Entry(width=10, justify='center', takefocus=1)
my_input1.grid(row=1, column=1)

result_label = Label(text='', bg='light grey', width=9, relief='ridge')
result_label.grid(row=3, column=1)

label1 = Label(text='=', width=9)
label1.grid(row=2, column=1)

ghost_label = Label(text='', width=10)
ghost_label.grid(row=0, column=0)

button = Button(text='Calculate', command=convert)
button.config(width=10, height=2)
button.grid(row=4, column=1)

window.bind('<Return>', lambda event=None: button.invoke())

tkvar1 = StringVar()
tkvar2 = StringVar()

options = ('Celsius', 'Fahrenheit')
tkvar1.set('Fahrenheit')
tkvar2.set('Celsius')

popupMenu1 = OptionMenu(window, tkvar1, *options)
popupMenu1.config(width=10)
popupMenu1.grid(row=1, column=2)

popupMenu2 = OptionMenu(window, tkvar2, *options)
popupMenu2.config(width=10)
popupMenu2.grid(row=3, column=2)

window.mainloop()