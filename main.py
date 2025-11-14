import sys
import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable) # type: ignore
    AsteroidField.containers = (updatable) # type: ignore
    Asteroid.containers = (updatable, drawable, asteroids) # type: ignore
    Shot.containers = (updatable, drawable, shots) # type: ignore
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collision(shot):
                        asteroid.split()
                        shot.kill()

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # Framerate limit
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
