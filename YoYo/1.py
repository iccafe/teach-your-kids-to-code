import turtle

t = turtle.Turtle()

t.shape("turtle")
c = t.clone()
n=10
while n <= 40:
    t.circle(n)
    n = n+10
t.fd(8)
t.stamp()

t.bk(10)
t.circle(90)
t.end_fill()