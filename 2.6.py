import turtle as t
t.shape('turtle')

def foo(n):
    for i in range(n):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.right(360/n)
        t.forward(50)
        t.stamp()

foo(12)