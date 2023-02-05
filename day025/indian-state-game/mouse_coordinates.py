import turtle

screen = turtle.Screen()
screen.title("India States Game")
image = "India-state.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coord(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coord)

turtle.mainloop()