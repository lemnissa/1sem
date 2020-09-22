import turtle as t
t.shape('turtle')

def foo(n):
    for i in range(10):
        t.penup()
        t.goto(10*i, 10*i)
        t.pendown()
        t.right(90)
        t.forward(20*i)
        t.right(90)
        t.forward(20*i)
        t.right(90)
        t.forward(20*i)
        t.right(90)
        t.forward(20*i)

foo(10)