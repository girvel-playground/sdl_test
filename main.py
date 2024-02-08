import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
while True:
    events = pygame.event.get()
    if any(event.type == pygame.QUIT for event in events): break

pygame.quit()
