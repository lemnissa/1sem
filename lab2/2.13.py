import turtle as t

def my_fill(col, R, tri=360):
    t.begin_fill()
    t.color(col)
    t.circle(R, tri)
    t.end_fill()
    
    t.color('black')    
    t.circle(R, tri)

    
t.shape("turtle")
t.up()
t.goto(0, -200)
t.down()

my_fill('yellow', 200) #лицо

t.up()                 #левый глаз
t.goto(-90, 60)
t.down()
my_fill('blue', 30)

t.up()                 #правый глаз
t.goto(90, 60)
t.down()
my_fill('blue', 30)

t.up()                 #нос
t.goto(0, 20)
t.down()
t.right(90)
t.width(12)
t.forward(50)


t.up()                 #рот
t.goto(-60, -100)
t.down()
t.color('red')    
t.circle(60, 180)

t.ht()