import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired"""
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        # Create a bullet rectangle at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        self.sound = pygame.mixer.Sound('sounds/bullet_sound.wav')
        self.sound.set_volume(ai_settings.bullet_volume)

    def update(self):
        """Moves bullet up the screen"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def sound_bullet(self):
        """Makes the bullet produce sound"""
        self.sound.play()
