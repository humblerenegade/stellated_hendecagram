import mod

mod.customize(mod.alef, "grey", 2)  # t1
mod.customize(mod.bet, "red", 2)   # t2
mod.customize(mod.gimel, "white", 2) # t3
mod.customize(mod.dalet, "grey", 2) # t4
mod.customize(mod.he, "white", 2)    # t5
mod.customize(mod.vav, "white", 2)   # t6

'''
# 22 point star
for i in range(11 * 2):
    mod.alef.forward(100)
    mod.alef.left(114.545)
'''

# turtle | stellation magnitude | length
def hendecagram(turtle, mag, ln):
    for i in range(11):
        turtle.forward(ln)
        turtle.left(65.454545 * mag)

'''
# Mid-cross grid
for i in range (4):
    mod.jump(mod.dalet, 0, 0)
    mod.dalet.forward(1920)
    mod.dalet.left(90)
'''

lena = -(200 / 2)
mod.jump(mod.bet, lena, -45)
hendecagram(mod.bet, 2, 200)

lenb = -(400 / 2)
mod.jump(mod.gimel, lenb, 30)
hendecagram(mod.gimel, 3, 400)

lenc = -(220 / 2)
mod.jump(mod.alef, lenc, -170)
hendecagram(mod.alef, 1, 220)

mod.w.exitonclick()
