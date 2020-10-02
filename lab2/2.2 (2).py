import turtle as t
t.shape('turtle')

def foo_1():
    t.penup()
    t.left(90)
    t.forward(20)
    t.pendown()
    t.right(45)
    t.forward(28.28)
    t.right(135)
    t.forward(40)
    t.penup()
    t.left(90)
    t.forward(10)
    t.pendown()

def foo_4():
    t.penup()
    t.left(90)
    t.forward(40)
    t.right(180)
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(180)
    t.forward(40)
    t.penup()
    t.left(90)
    t.forward(10)
    t.pendown()

def foo_7():
    t.left(90)
    t.forward(20)
    t.right(45)
    t.forward(28.28)
    t.left(135)
    t.forward(20)
    t.penup()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.pendown()

def foo_0():
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.penup()
    t.left(90)
    t.forward(30)
    t.pendown()

def draw(i):
    for i in x:
        if i=='1':
            foo_1()
        if i=='4':
            foo_4()
        if i=='7':
            foo_7()
        if i=='0':
            foo_0()

x = '141700'
draw(x)