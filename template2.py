import pygame
import random
import time
import math


def main():
    width = 700
    height = 700
    FPS = 30
    vec = pygame.math.Vector2
    
    blue_color = (97, 159, 182) 
    black_color = (0, 0, 0)

    hero_acc = 0.5
    hero_fric = -0.10
    hero_grav = 0.8
    pic = pygame.image.load

    

    font_name = pygame.font.match_font('Times New Roman')
    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, black_color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    class Hero(pygame.sprite.Sprite):
        def __init__(self, platforms):
            pygame.sprite.Sprite.__init__(self)
            self.platforms = platforms
            self.walking = False
            self.jumping = False
            self.current_frame = 0
            self.last_update = 0
            self.load_images()
            self.image = self.walk_frames_r[0] 
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.radius = 45
            self.rect = self.image.get_rect()
            self.rect.center = (width / 2, height / 2)
            self.pos = vec(width / 2, height / 2)
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)

        def load_images(self):
            self.standing_frames = [pic('images/idle1.png'), pic('images/idle2.png')]
            self.walk_frames_r = [pic('images/walk1.png'), pic('images/walk2.png')]
            self.walk_frames_l = []
            for frame in self.walk_frames_r:
                self.walk_frames_l.append(pygame.transform.flip(frame, True, False))
            self.jump_frame = [pic('images/Jump1.png'), pic('images/Jump2.png')]


        def jump(self):
            self.rect.x += 1 
            hits = pygame.sprite.spritecollide(self, self.platforms, False)
            self.rect.x -= 1
            if hits:
                self.vel.y = -20

        def update(self):
            self.animate()
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
        
        def animate(self):
            now = pygame.time.get_ticks()
            if self.vel.x != 0:
                self.walking = True
            else:
                self.walking = False
            #walk animation
            if self.walking:
                if now - self.last_update > 200:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                    if self.vel.x > 0:
                        self.image = self.walk_frames_r[self.current_frame]
                    else:
                        self.image = self.walk_frames_l[self.current_frame]
            #idle animation
            if not self.jumping and not self.walking:
                if now - self.last_update > 350:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                    self.image = self.standing_frames[self.current_frame]
            self.image = pygame.transform.scale(self.image, (100, 100))
            
                

    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images/fish.png')
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.radius = 15
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

    class Shield(Mob):
        def __ini__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image

        
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
    hero = Hero(platforms)    
    all_sprites.add(hero)
    all_sprites.add(p1)
    platforms.add(p1)
    for i in range(10):
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
        hits = pygame.sprite.spritecollide(hero, mobs, False, pygame.sprite.collide_circle)
        if hits:
            running = False

        p_hits = pygame.sprite.spritecollide(hero, platforms, False)
        if p_hits:
            hero.pos.y = p_hits[0].rect.top
            hero.vel.y = 0

        # draw / render
        screen.fill(blue_color)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(pygame.time.get_ticks() / 1000), 30, width / 2, 10)
        # after drawing everything
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()   
