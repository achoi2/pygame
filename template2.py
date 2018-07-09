import pygame
import random

def main():
    width = 500
    height = 500
    FPS = 30

    blue_color = (97, 159, 182) 
    black_color = (0, 0, 0)

    class Hero(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images/hero.png')
            self.rect = self.image.get_rect()
            self.rect.center = (width / 2, height / 2)
            self.speedx = 0
            self.speedy = 0 

        def update(self):
            self.speedx = 0
            self.speedy = 0
            keystate = pygame.key.get_pressed()   
            if keystate[pygame.K_LEFT] and self.rect.x > self.speedx:
                self.rect.x -= 5
            if keystate[pygame.K_RIGHT] and self.rect.x < width - 32 - self.speedx:
                self.rect.x += 5
            if keystate[pygame.K_UP] and self.rect.y > self.speedy:
                self.rect.y -= 5
            if keystate[pygame.K_DOWN] and self.rect.y < height - 32 - self.speedy: 
                self.rect.y += 5

    class Monster(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images/monster.png')
            self.rect = self.image.get_rect()
            self.rect.x = 200
            self.rect.y = 200
            self.speedy = 2
            self.speedx = 5

        def update(self):          
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.right > width:
                self.rect.right = 0
            if self.rect.bottom > height:
                self.rect.bottom = 0
            if self.rect.left > width:
                self.rect.left = 0
            if self.rect.top > height:
                self.rect.top = 0
            # self.rect.y += self.speedy
            # if self.rect.right > width:
            #     self.rect.left = 0
            # if self.rect.left < width:
            #     self.rect.right = 0
            
    
    
    
    # initialize and create window 
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch the monster')
    clock = pygame.time.Clock()

    background = pygame.image.load('images/background.png')
    background = pygame.transform.scale(background, (height, width))
    background_rect = background.get_rect()
    
    all_sprites = pygame.sprite.Group()
    hero = Hero()
    monster = Monster()
    all_sprites.add(hero, monster)
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
        # draw / render
        screen.fill(blue_color)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        # after drawing everything
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()   