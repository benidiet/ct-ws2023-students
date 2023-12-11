import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

def handle_keys():
    running = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    return running

def main():
    pygame.init()
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    clock = pygame.time.Clock()

    delta_t = 0

    running = True
    while running:
        # Clear
        screen.fill("black")

        # Input handling
        running = handle_keys()

        # Update object positions
        # TODO

        # Draw objects
        pygame.draw.circle(
            surface=screen,
            color=(0,255,0),
            center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2),
            radius=10)
        
        # Show
        pygame.display.update()

        # Wait and get elapsed time
        delta_t = clock.tick(60)

if __name__ == '__main__':
    main()


# In der folgenden Aufgabe sollen Sie das Spiel Pong entwickeln. 
