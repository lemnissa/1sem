import turtle as t


t.shape('turtle')

def draw_number(n):
    if n == '0':
        for line in zero:
            eval(line.rstrip())            
    elif n == '1':
        for line in one:
            eval(line.rstrip())        
    elif n == '4':
        for line in four:
            eval(line.rstrip())
    elif n == '7':
        for line in seven:
            eval(line.rstrip())
    else:
        print('nope')

with open('n0.txt') as file:
    zero = file.readlines()
with open('n1.txt') as file:
    one = file.readlines()    
with open('n4.txt') as file:
    four = file.readlines()
with open('n7.txt') as file:
    seven = file.readlines()
    
t.penup()
t.goto(-350, 300)
t.pendown()    

nums = list('141700')
for x in nums:
    t.pendown()    
    draw_number(x)
    t.penup()        
    t.forward(60)
    
