import turtle as t

x_max, y_max = 300, 300
t.penup()
t.forward(x_max)
t.pendown()
t.right(90)
t.forward(y_max)
t.right(90)
t.forward(x_max*2)
t.right(90)
t.forward(y_max*2)
t.right(90)
t.forward(x_max*2)
t.right(90)
t.forward(y_max)
t.penup()
t.goto(0, 0)
t.pendown()


ay = -9.8
dt = 0.1

x, y, Vx, Vy = 0, 0, 10, 0

while True:
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2 
    Vy += ay*dt
    t.goto(x, y)
    if abs(y) >= y_max:
        Vy *= -1
    if abs(x) >= x_max:
        Vx *= -1
    