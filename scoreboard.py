from pygame.sysfont import SysFont
from pygame.sprite import Group

from ship import Ship


# the score board that goes on the top of the screen and updates
class Scoreboard:

    def __init__(self, ai_settings, screen, stats):
        # creates the scoreboard
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # Font settings for score information
        self.text_color = (255, 255, 0)
        self.font = SysFont(None, 48)
        # initial score image
        self.score_image = None
        self.score_rect = None
        # high score image
        self.high_score_image = None
        self.high_score_rect = None
        # level image
        self.level_image = None
        self.level_rect = None
        # ships left
        self.ships = None
        # initialize score, high score, level, ships
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = 'Score: {:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # Display the score in the top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = 'High Score: {:,}'.format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        # Center high score at top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render('Level: ' + str(self.stats.level), True, self.text_color,
                                            self.ai_settings.bg_color)
        # Position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * (ship.rect.width + 5)
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships
        self.ships.draw(self.screen)
