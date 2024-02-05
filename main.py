import sdl2.ext

sdl2.ext.init()
window = sdl2.ext.Window("Hello world!", size=(640, 480))
window.show()

while True:
    events = sdl2.ext.get_events()
    if any(e.type == sdl2.SDL_QUIT for e in events): break
    window.refresh()

sdl2.ext.quit()
