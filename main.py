import pygame

class Runtime:

    def __init__(self, level):
        pygame.init()

        # General
        self.clock = pygame.time.Clock()

        # Enemies
        self.enemy_queue = []
        self.enemy_list = pygame.sprite.Group()


    def run(self):
        running = True
        while running:

            # Set the game to 60 FPS
            self.clock.tick(60)

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)

            # Draw the background
            self.game_board.draw()

            # Draw the overlay trees
            self.game_board.draw_trees()

            # Update game display
            pygame.display.update()
        pygame.quit()