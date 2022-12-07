import pyglet


window = pyglet.window.Window(fullscreen=True)

label = pyglet.text.Label('Vitaly, hello',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    label.draw()
    sound = pyglet.media.load('sam.wav')
    sound.play()


if __name__ == '__main__':
    pyglet.app.run()