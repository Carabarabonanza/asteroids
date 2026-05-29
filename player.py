import pygame
from shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_a]:
            self.rotate(-dt)
        if self.keys[pygame.K_d]:
            self.rotate(dt)
        if self.keys[pygame.K_w]:
            self.move(dt)
        if self.keys[pygame.K_s]:
            self.move(-dt) 
        if self.keys[pygame.K_SPACE]:
            self.shoot()
        self.timer -= dt
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        
    def shoot(self):
         if self.timer > 0:
            return
         self.timer = PLAYER_SHOOT_COOLDOWN_SECONDS
         unit_vector = pygame.Vector2(0, 1)
         rotated_vector = unit_vector.rotate(self.rotation)
         shoot_speed = rotated_vector * PLAYER_SHOOT_SPEED
         my_shot = Shot(self.position.x, self.position.y)
         my_shot.velocity = shoot_speed
        
         
