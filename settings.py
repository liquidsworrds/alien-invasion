class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (179, 224, 242)

        # Ship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet
        self.bullet_speed_factor = 2
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = 255, 95, 31
        self.bullets_allowed = 3

        # Alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 8
        # fleet_direction -> 1 means right & -1 means left
        self.fleet_direction = 1

        # Game
        self.speedup_scale = 0.6
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.8

        # 1 is right -1 is left
        self.fleet_direct = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor += self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
