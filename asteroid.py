#type: ignore
import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_direction_positive = self.velocity.rotate(angle)
        new_direction_negative = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_positive = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_positive.velocity = new_direction_positive * 1.2
        asteroid_negative = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_negative.velocity = new_direction_negative * 1.2

