import pygame
import random
import math

class target:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.lower_x = 0
        self.upper_x = 8000 # Chosen arbitrarily to be larger than most screen sizes
        self.lower_y = 0
        self.upper_y = 8000
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_radius(self):
        return self.radius
    
    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius / 1.5)
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.radius / 3)
    
    def set_random_position_bounds(self, lower_x, upper_x, lower_y, upper_y):
        self.lower_x = lower_x
        self.upper_x = upper_x
        self.lower_y = lower_y
        self.upper_y = upper_y

    def random_position(self):
        self.x = random.randint(self.lower_x + self.radius, self.upper_x - self.radius)
        self.y = random.randint(self.lower_y + self.radius, self.upper_y - self.radius)

    def dist_from_center(self, x, y):
        whole_x = abs(self.x - x)
        whole_y = abs(self.y - y)
        return math.sqrt(whole_x ** 2 + whole_y ** 2)