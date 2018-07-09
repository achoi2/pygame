import pygame

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    black_color = (0, 0, 0)
    pygame.mixer.init()
    sound = pygame.mixer.Sound('../sounds/win.wav')
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Simple Example')

    clock = pygame.time.Clock()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound.play()
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True


        # Draw background
        screen.fill(blue_color)

        # Game display

        font = pygame.font.Font(None, 25)
        text = font.render('Click to play a sound', True, black_color)
        screen.blit(text, (160, 230))

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
