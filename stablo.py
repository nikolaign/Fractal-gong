import turtle
t = turtle.Turtle()
t.left(90)
t.backward(133)
t.color("green")
t.speed(108)
t.clone()



perc = 0.7
angle = 33.0
shortest = 10

def fract(n):
    if n >= shortest:
        t.forward(n)
        t.right(angle)
        fract(n * perc * 0.8)
        t.left(angle)
        fract(n * perc)
        t.left(angle)
        fract(n * perc * 0.8)
        t.right(angle)
        t.backward(n)
fract(133)


