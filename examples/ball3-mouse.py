import pygame

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.radius = 50

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x + self.radius > width:
            self.speed_x = -5
        if self.y + self.radius > height:
            self.speed_y = -5
        if self.x - self.radius < 0:
            self.speed_x = 5
        if self.y - self.radius < 0:
            self.speed_y = 5

    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Simple Example')

    # Game initialization
    ball_list = [
        Ball(50, 50)
    ]
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                ball_list.append(Ball(x, y))
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        # Game logic
        for ball in ball_list:
            ball.update(width, height)

        # Draw background
        screen.fill(blue_color)

        # Game display
        for ball in ball_list:
            ball.render(screen)

        font = pygame.font.Font(None, 25)
        text = font.render('Click to add a ball', True, (0, 0, 0))
        screen.blit(text, (80, 230))

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
