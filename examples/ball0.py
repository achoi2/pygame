import pygame

def main():
    canvas_width = 800
    canvas_height = 600

    pygame.init()
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    pygame.display.set_caption("Ball Example")

    ball_y = 100
    ball_x = 100
    ball_radius = 50
    ball_dir_x = 5
    ball_dir_y = 5
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius, 0)
        pygame.display.update()
        ball_x += ball_dir_x
        ball_y += ball_dir_y
        if ball_x + ball_radius > canvas_width:
            ball_dir_x = -ball_dir_x
        if ball_y + ball_radius > canvas_height:
            ball_dir_y = -ball_dir_y
        if ball_x - ball_radius < 0:
            ball_dir_x = -ball_dir_x
        if ball_y - ball_radius < 0:
            ball_dir_y = -ball_dir_y

    pygame.quit()

main()
