from pygame import sprite, Surface, PixelArray
from random import randrange


class BunkerBlock(sprite.Sprite):
    # bunker block
    def __init__(self, ai_settings, screen, row, col):
        super().__init__()
        self.screen = screen
        self.height = ai_settings.bunker_block_size
        self.width = ai_settings.bunker_block_size
        self.color = ai_settings.bunker_color
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col
        self.dmg = False

    def damage(self, top):
        # make pixels transparent to represent damage
        if not self.dmg:
            px_array = PixelArray(self.image)
            if top:
                for i in range(self.height * 3):
                    px_array[randrange(0, self.width - 1),
                             randrange(0, self.height // 2)] = (0, 0, 0, 0)  # transparent pixel
            else:
                for i in range(self.height * 3):
                    px_array[randrange(0, self.width - 1),
                             randrange(self.height // 2, self.height - 1)] = (0, 0, 0, 0)   # transparent pixel
            self.dmg = True
        else:
            self.kill()

    def update(self):
        self.screen.blit(self.image, self.rect)


def make_bunker(ai_settings, screen, position):
    # creates bunkers
    bunker = sprite.Group()
    for row in range(5):
        for col in range(9):
            # Don't draw full rows of blocks on last two rows
            # Don't draw full rows of blocks on the top row
            # Gives the bunker its signature shape
            if not ((row > 3 and (1 < col < 7)) or
                    (row > 2 and (2 < col < 6)) or
                    (row == 0 and (col < 1 or col > 7))):
                block = BunkerBlock(ai_settings, screen, row, col)
                block.rect.x = int(ai_settings.screen_width * 0.15) + (250 * position) + (col * block.width)
                block.rect.y = int(ai_settings.screen_height * 0.8) + (row * block.height)
                bunker.add(block)
    return bunker
