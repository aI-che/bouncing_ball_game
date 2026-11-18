import pygame
import sys
import random

from game_portal import PortalSys

class Game:
 
    def __init__(self):
        pygame.init()
        self.screen_width = 900 
        self.screen = pygame.display.set_mode((self.screen_width, 600))
        self.clk = pygame.time.Clock()
        self.y = 500
        self.x = 450
        self.floor_y = 550
        self.ver_speed = 0
        self.move_speed = 400
        self.gravity = 0.8
        self.ball_strength = -15 
        self.isrun = True
        self.radius = 20
        self.width = 20
        self.portals = PortalSys(self)
        
    def game_update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isrun = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and self.y >= self.floor_y - self.radius:
                    self.ver_speed = self.ball_strength
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += self.move_speed * dt 
        if keys[pygame.K_a]:
            self.x -= self.move_speed * dt 

    
        if self.x > self.screen_width + self.radius:
            self.x = -self.radius

        elif self.x < -self.radius:
            self.x = self.screen_width + self.radius
           
        self.ver_speed += self.gravity
        self.y += self.ver_speed

        if self.y >= self.floor_y - self.radius:
            self.y = self.floor_y - self.radius
            self.ver_speed = 0
            self.move_speed = 400


        self.portals.game_portal_update()



    def game_draw(self):

        self.screen.fill((0, 0, 0))
        self.portals.game_portal_draw()
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.floor_y), (self.screen_width, self.floor_y), 5)
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius, self.width)
        pygame.display.flip()
  

    def run(self):
       while self.isrun:
           dt = self.clk.tick(60) / 1000.0
           self.game_update(dt)
           self.game_draw()

       pygame.quit()
       sys.exit()

game = Game()
game.run()
