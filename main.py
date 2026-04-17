import pygame
from logger import log_state
from constants import *
from player import *

def main():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_1 = Player(x, y, PLAYER_RADIUS)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_1.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick() / 1000
        # print(dt)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
