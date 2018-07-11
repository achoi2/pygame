import pygame
import random
import time
import math


def main():
    width = 500
    height = 500
    FPS = 30
    vec = pygame.math.Vector2
    
    blue_color = (97, 159, 182) 
    black_color = (0, 0, 0)

    hero_acc = 0.5
    hero_fric = -0.12
    hero_grav = 0.8

    class Hero(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.platforms = platforms
            self.image = pygame.image.load('images/cat.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (width / 2, height / 2)
            self.pos = vec(width / 2, height / 2)
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)

        def jump(self):
            self.vel.y = -20

        def update(self):
            self.acc = vec(0, hero_grav)
            keys = pygame.key.get_pressed()   
            if keys[pygame.K_LEFT]:
                self.acc.x = -hero_acc
            if keys[pygame.K_RIGHT]:
                self.acc.x = hero_acc
            
            self.acc.x += self.vel.x * hero_fric
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc

            if self.pos.x > width:
                self.pos.x = 0
            if self.pos.x < 0:
                self.pos.x = width

            self.rect.midbottom = self.pos

    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images/fish.png')
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = random.randrange(2, 8)
            

        def update(self):          
            self.rect.y += self.speedy

            if self.rect.top > height + 10:
                self.rect.x = random.randrange(width - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 8)
        
    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, w, h):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((w, h))
            self.image.fill(blue_color) 
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y                         
    # initialize and create window 
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Cat')
    clock = pygame.time.Clock()

    background = pygame.image.load('images/snow.jpg')
    background = pygame.transform.scale(background, (height, width))
    background_rect = background.get_rect()
    
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    p1 = Platform(0, height, width, 0)
    hero = Hero()    
    all_sprites.add(hero)
    all_sprites.add(p1)
    platforms.add(p1)
    for i in range(8):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
 
    # game loop
    running = True
    while running:
        clock.tick(FPS)
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hero.jump()
            

        # update
        all_sprites.update()
        
        #collision
        # hits = pygame.sprite.spritecollide(hero, mobs, False)
        # if hits:
        #     running = False

        p_hits = pygame.sprite.spritecollide(hero, platforms, False)
        if p_hits:
            hero.pos.y = p_hits[0].rect.top
            hero.vel.y = 0

        # draw / render
        screen.fill(blue_color)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        # after drawing everything
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()   