from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_1_velocity = self.velocity.rotate(random_angle)
        split_asteroid_2_velocity = self.velocity.rotate(-random_angle)
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
        split_asteroid_1.velocity = split_asteroid_1_velocity * 1.2
        split_asteroid_2.velocity = split_asteroid_2_velocity * 1.2
