import turtle as t

def foo(n, a):
    for i in range(n):
        ang = 180 - 180/n
        t.forward(a)
        t.right(ang)
        t.forward(a)

t.speed(10)

t.up()
t.goto(-150, 0)
t.down()
foo(5, 100)

t.up()
t.goto(150, 0)
t.down()
foo(11, 100)

t.ht()