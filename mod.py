import turtle
w = turtle.Screen()
w.bgcolor("black")
w.setup(1920, 1080, startx=None, starty=-519)

# Ordinal values gematria 27letters
alef = turtle.Turtle()   # א
bet = turtle.Turtle()    # ב
gimel = turtle.Turtle()  # ג
dalet = turtle.Turtle()  # ד
he = turtle.Turtle()     # ה
vav = turtle.Turtle()    # ו
zayin = turtle.Turtle()  # ז
xet = turtle.Turtle()    # ח
tet = turtle.Turtle()    # ט
yod = turtle.Turtle()    # י
kaf = turtle.Turtle()    # כ | ך
lamed = turtle.Turtle()  # ל
mem = turtle.Turtle()    # מ | ם
nun = turtle.Turtle()    # נ | ן
samekh = turtle.Turtle() # ס
ayin = turtle.Turtle()   # ע
pe = turtle.Turtle()     # פ | ף
tsadi = turtle.Turtle()  # צ | ץ
qof = turtle.Turtle()    # ק
resh = turtle.Turtle()   # ר
shin = turtle.Turtle()   # ש
tav = turtle.Turtle()    # ת


def customize(turtle, clr, sz):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(sz)
    turtle.color(clr)

def jump(turtle, x_pos, y_pos):
    turtle.up()
    turtle.goto(x_pos, y_pos)
    turtle.down()
