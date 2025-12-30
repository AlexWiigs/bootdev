""" 
code copied from: https://www.boot.dev/lessons/a56fface-8a77-40ee-bf17-50d76078e5ec 

In your Player class, add a new method called shoot. This method takes no parameters and does the following:
    Creates a new Shot at the current position of the player.
    Sets the shot's .velocity attribute:
        Start with a pygame.Vector2 of (0, 1).
        .rotate() the vector in the direction the player is facing.
        Scale it up (multiply by PLAYER_SHOOT_SPEED) to make it move faster.

In your Player class, handle the spacebar (pygame.K_SPACE) and call the shoot method when it's pressed.

Run your game for at least a few seconds, and fire some shots. Make sure the bullets are being created and moving in the correct direction.

"""
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= self.radius + other.radius:
            return True
        return False
