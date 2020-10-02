import turtle as t
from numpy import sin, pi

R = 20
t.shape('turtle')
t.left(180)

def fig(R, n):
    triangle = 180*(n-2)/n
    t.right(triangle/2)    
    for _ in range(n):
        t.forward(2*(R*n-5)*sin(pi/n))        
        t.left(180-triangle) 
    t.left(triangle/2)    
    #t.right(180-triangle/2)

for n in range(3, 10):
    fig(R, n)
    t.penup()
    t.backward(R-2)
    t.pendown()
    