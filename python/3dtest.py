# the first 6 lines below will create a black Window
import pyglet
win = pyglet.window.Window()
@win.event
def on_draw():
    win.clear()
pyglet.app.run()
# window process stops here
# from here we are going to draw a few lines
import pyglet
from pyglet.gl import *
win = pyglet.window.Window()
@win.event
def on_draw():
    # Clear buffers
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw some stuff here
    glBegin(GL_POINTS)
    glVertex2i(50, 50)
    glVertex2i(75, 100)
    glVertex2i(100, 150)
    glEnd()
pyglet.app.run()
# dot drawing process stops here
# from here down is lines
import pyglet
from pyglet.gl import *
win = pyglet.window.Window()
@win.event
def on_draw():
    # Clear buffers
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw some stuff
    glBegin(GL_LINE_LOOP)
    glVertex2i(50, 50)
    glVertex2i(70, 100)
    glVertex2i(100, 150)
    glVertex2i(200, 200)
    glEnd()
pyglet.app.run()
# end line drawing here
#
