import turtle

s = turtle.getscreen()
t = turtle.Turtle()

z=5
c=["red","yellow","blue","black"]
r=50
for i in range(4):

    t.pensize(z)
    t.pencolor(c[i])
    t.circle(r)    
    r+=20
    z+=5
t.penup()
t.goto(-70,-50)
t.pensize(5)
t.pencolor("navy")
def sq(side):
    for x in range(4):
        t.fd(side)
        t.lt(90)

t.pendown()
sq(100)

s.mainloop()    