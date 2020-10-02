import turtle as t

t.shape('turtle')
t.speed(10)


def foo():
   for _ in range(180):
       t.forward(2)
       t.left(2)

n = 6
for i in range(n):
   t.left(360/n)
   foo()