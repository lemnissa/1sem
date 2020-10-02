import numpy as np

import turtle as t
t.shape('turtle')

t.goto(0, 0)

def foo(n):
    for i in range(n):

        t.right(1)
        n_r = i * np.pi / 180
        t.forward(0.01*(n_r * (1 + (n_r)**2)**(0.5) + np.log(n_r + (1 + (n_r)**2)**(0.5))))

foo(3600)