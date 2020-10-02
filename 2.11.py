import turtle as t

t.shape('turtle')
t.speed(10)
t.left(90)

def foo(i):
   for _ in range(180):
       t.forward(i/2)
       t.left(2)

n = 3
for i in range(1, 2*n+1):
   foo(i)
   t.left(180)
   foo(i)
   t.left(180)