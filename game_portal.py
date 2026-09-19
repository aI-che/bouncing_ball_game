import pygame


class PortalSys:

    def __init__(self, game_instance):

        self.game = game_instance

        self.portal_a = pygame.Rect(100, 375, 20, 50)
        self.portal_b = pygame.Rect(700, 375, 20, 50)

        self.ballrect = pygame.Rect(
            self.game.x - self.game.radius,
            self.game.y - self.game.radius,
            self.game.radius * 2,
            self.game.radius * 2
        )

        # Teleporttan hemen sonra tekrar teleport olmasını engeller
        pygame.time.wait(100)
        self.can_teleport = True

    def game_portal_update(self):

        self.ballrect = pygame.Rect(
            self.game.x - self.game.radius,
            self.game.y - self.game.radius,
            self.game.radius * 2,
            self.game.radius * 2
        )

        # Top artık hiçbir portalın içinde değilse
        # tekrar teleport edilebilir
        if not self.ballrect.colliderect(self.portal_a) and \
           not self.ballrect.colliderect(self.portal_b):
            self.can_teleport = True

        if self.can_teleport:

            # YEŞİL -> MAVİ
            if self.ballrect.colliderect(self.portal_a):

                self.game.x = self.portal_b.right + self.game.radius
                self.game.y = self.portal_b.centery
                self.game.move_speed = -self.game.move_speed

                self.can_teleport = False

            # MAVİ -> YEŞİL
            elif self.ballrect.colliderect(self.portal_b):

                self.game.x = self.portal_a.left - self.game.radius
                self.game.y = self.portal_a.centery
                self.game.move_speed = -self.game.move_speed

                self.can_teleport = False

    def game_portal_draw(self):

        pygame.draw.rect(
            self.game.screen,
            (0, 255, 0),
            self.portal_a
        )

        pygame.draw.rect(
            self.game.screen,
            (0, 0, 255),
            self.portal_b
        )