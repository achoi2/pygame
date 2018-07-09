import pygame

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    black_color = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Simple Example')
    clock = pygame.time.Clock()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                print 'mouse down at %d, %d' % event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                print 'mouse up at %d, %d' % event.pos
            if event.type == pygame.KEYUP:
                print 'key up %r' % event.key
            if event.type == pygame.KEYDOWN:
                print 'key down %r' % event.key
            if event.type == pygame.QUIT:
                stop_game = True


        # fill background color
        screen.fill(blue_color)

        # Game display
        font = pygame.font.Font(None, 25)
        text = font.render('Click or type and see events in the terminal', True, black_color)
        screen.blit(text, (80, 230))


        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
