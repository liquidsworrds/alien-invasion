class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (179, 224, 242)
        # self.bg_color = (230, 230, 230)

        # Ship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet
        self.bullet_speed_factor = 3
        self.bullet_width = 14
        self.bullet_height = 14
        self.bullet_color = 255, 95, 31
        self.bullets_allowed = 3

        # Alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction -> 1 means right & -1 means left
        self.fleet_direction = 1
