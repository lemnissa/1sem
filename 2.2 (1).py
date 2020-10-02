import turtle as t
t.shape('turtle')

from random import *

def foo(n):
    for i in range(n):
         t.forward(randint(10, 30))
         t.left(randint(0, 360))

foo(100)