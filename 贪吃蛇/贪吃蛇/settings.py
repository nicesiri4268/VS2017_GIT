
class Settings():
    def __init__(self):
        self.screen_wight = 1200
        self.screen_height = 800
        self.screen_color = (255,255,255)

        self.rect_wight = 60
        self.rect_height = 10
        self.rect_color = (0,0,0)
        self.rect_spreed = 2

        self.snake_x = int(self.screen_wight) / 2
        self.snake_y = int(self.screen_height) / 2
