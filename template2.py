import pygame
import random
import time
import math

def main():
    width = 500
    height = 500
    FPS = 30

    blue_color = (97, 159, 182) 
    black_color = (0, 0, 0)

    class Hero(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images/dog.png')
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()
            self.rect.centerx = width / 2
            self.rect.bottom = height
            self.speedx = 0

        def update(self):
            self.speedx = 0
            keystate = pygame.key.get_pressed()   
            if keystate[pygame.K_LEFT] and self.rect.x > self.speedx:
                self.rect.x -= 5
            if keystate[pygame.K_RIGHT] and self.rect.x < width - 64 - self.speedx:
                self.rect.x += 5
            

    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images/cat.png')
            self.image = pygame.transform.scale(self.image, (64, 64))
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
        
                                
    # initialize and create window 
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch the monster')
    clock = pygame.time.Clock()

    background = pygame.image.load('images/snow.jpg')
    background = pygame.transform.scale(background, (height, width))
    background_rect = background.get_rect()
    
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    hero = Hero()
    all_sprites.add(hero)
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

        # update
        all_sprites.update()
        
        #collision
        hits = pygame.sprite.spritecollide(hero, mobs, False)
        if hits:
            running = False

        # draw / render
        screen.fill(blue_color)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        # after drawing everything
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()   