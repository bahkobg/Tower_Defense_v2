import pygame
import game_board


class Runtime:

    def __init__(self):
        pygame.init()

        # General
        self.clock = pygame.time.Clock()
        self.main_menu_opened = False
        self.game_started = True
        self.options_opened = False
        self.paused = False
        self.game_board = game_board.GameBoard()
        self.difficulty = 1

        # Enemies
        self.enemy_queue = []
        self.enemy_list = pygame.sprite.Group()

    def restart(self):
        pass

    def spawn_enemy(self):
        pass

    def setup_wave(self):
        pass

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

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()

            # Draw the background
            self.game_board.draw()

            # Draw the overlay trees
            self.game_board.draw_trees()

            # Update game display
            pygame.display.update()
        pygame.quit()



if __name__ == '__main__':
    g = Runtime()
    g.run()
