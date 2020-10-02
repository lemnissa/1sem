import numpy as np

import turtle as t
t.shape('turtle')

t.goto(0, 0)

def foo(n):
    for i in range(n):

        t.forward(10*i)
        t.left(90)
        t.forward(10*i)
        t.left(90)
        
foo(36)