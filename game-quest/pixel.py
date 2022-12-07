import pyglet
from pyglet import shapes
from pyglet.window import key, mouse

window = pyglet.window.Window(resizable=True)
image = pyglet.resource.image('monkey.jpg')
music = pyglet.resource.media('sam.wav')
circle = shapes.Circle(x=100, y=150, radius=100, color=(50, 225, 30))
square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        circle = shapes.Circle(x=100, y=150, radius=100, color=(50, 225, 30))
        circle.draw()
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        circle.draw()
        print('The left mouse button was pressed.')

    if button == mouse.RIGHT:
        print('The right mouse button was pressed.')


@window.event
def on_draw():
    window.clear()
    #image.blit(0, 0)




#music.play()
pyglet.app.run()
