"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Adi Sethupathy.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
size = 100

adi = rg.SimpleTurtle('turtle')
adi.pen = rg.Pen('red', 5)
adi.speed = 15

mo = rg.SimpleTurtle()
mo.pen = rg.Pen('blue', 40)
mo.speed = adi.speed

for k in range(20):
    adi.draw_circle(size)

    adi.pen_up()
    adi.forward(10)
    adi.pen_down()


    mo.draw_square(size)
    mo.pen_up()
    mo.forward(10)
    mo.pen_down()
    size = size - 12


window.close_on_mouse_click()

