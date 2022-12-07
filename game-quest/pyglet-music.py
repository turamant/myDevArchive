import pyglet

music = pyglet.resource.media('sam.wav')
music.play()


pyglet.app.run()