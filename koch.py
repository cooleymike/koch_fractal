#koch fractals with turtle
import turtle

def setup(pencil):
    pencil.color('blue')
    pencil.penup()
    pencil.goto(-200,100)
    pencil.pendown()

#lets draw the flake!
def koch(pencil, size, order):
    if order == 0:
        pencil.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(pencil, size/3, order-1)
            pencil.left(angle)

def main():
    pencil = turtle.Turtle()
    setup(pencil)
    turtle.tracer(100)

    order = 7
    size = 400

    for i in range(3):
        koch(pencil, size, order)
        pencil.right(120)

if __name__ == '__main__':
    main()
    turtle.tracer(100)
    turtle.mainloop()
