# type: ignore
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_COLOR, SCREEN_FPS
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(SCREEN_COLOR)
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            for shot in shots:
                if shot.colide(obj):
                    shot.kill()
                    obj.split()
            if player.colide(obj):
                print("Game over!")
                return
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(SCREEN_FPS) / 1000

if __name__ == "__main__":
    main()