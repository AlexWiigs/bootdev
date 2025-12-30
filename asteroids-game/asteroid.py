"""
asteroid.py

    Create two new Asteroid objects at the current asteroid position with the new
    radius.

    Set the first's .velocity to the first new vector, but make it move faster by
    scaling it up (multiplying) by 1.2.

    Do the same for the second asteroid, but with the second new vector.

    Run the game and shoot some asteroids!

"""
import random
import pygame
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity1, velocity2 = self.velocity.rotate(angle) * 1.2, self.velocity.rotate(-angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity, asteroid2.velocity = velocity1, velocity2

