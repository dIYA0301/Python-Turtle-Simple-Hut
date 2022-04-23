from turtle import*
speed(0)

#ground
bgcolor('green')

#sky
penup()
goto(-400,-200)
pendown()
color('light blue')
begin_fill()
for i in range(2):
    forward(1000)
    left(90)
    forward(2000)
    left(90)
end_fill()

#cloud
penup()
goto(300,200)
pendown()
color('white')
begin_fill()
circle(30)
end_fill()

penup()
goto(320,220)
pendown()
color('white')
begin_fill()
circle(30)
end_fill()

penup()
goto(300,250)
pendown()
color('white')
begin_fill()
circle(30)
end_fill()

#sun
penup()
goto(-300,200)
pendown()
color('yellow')
begin_fill()
circle(40)
end_fill()

#hut
penup()
goto(-100,-200)
pendown()
color('orange')
pensize(2)
begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()

#roof
penup()
goto(-114,0)
pendown()
color('brown')
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

#chimney
penup()
goto(30,70)
pendown()
color('brown')
begin_fill()
for i in range(2):
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

#door
penup()
goto(-30,-200)
pendown()
color('red')
begin_fill()
for i in range(2):
    forward(60)
    left(90)
    forward(90)
    left(90)
end_fill()

#doorknob
penup()
goto(-20,-160)
pendown()
color('black')
begin_fill()
circle(6)
end_fill()

#window1
penup()
goto(-75,-90)
pendown()
color("black", "white")
begin_fill()
for i in range(4):
    forward(60)
    left(90)
end_fill()

#window1- horizontal line
penup()
goto(-75,-60)
pendown()
color("black")
forward(60)

#window1- vertical line
penup()
goto(-45,-90)
pendown()
left(90)
color("black")
forward(60)

#window2
penup()
goto(75,-90)
pendown()
color("black", "white")
begin_fill()
for i in range(4):
    forward(60)
    left(90)
end_fill()

#window2- horizontal line
penup()
goto(75,-60)
pendown()
left(90)
color("black")
forward(60)

#window2- vertical line
penup()
goto(45,-90)
pendown()
right(90)
color("black")
forward(60)
