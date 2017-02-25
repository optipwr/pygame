import pygame;
# this will get the sprite class from pygame.sprite. Our hero will be a sprite object
from pygame.sprite import Sprite;

class Hero(Sprite):
    # initialize class properties
    def __init__(self, screen, game_settings):
        super(Hero,self).__init__();
        self.image = pygame.image.load('bunny.jpeg');
        self.image = pygame.transform.scale(self.image,(100,160));
        self.screen = screen;
        # create a rect prop that will be the dimentions and location of the image
        self.rect = self.image.get_rect();
        # Now that we have the screen object from main, get the screen size
        self.screen_rect = screen.get_rect();
        print self.screen_rect;
        # this will put the middle of the her at the middle of the screen
        self.rect.centery = self.screen_rect.centery
        # this will put the left side of our hero at the left side of our screen
        self.rect.left = self.screen_rect.left;
        # set up movement booleans. All are false by default
        self.moving_right = False;
        self.moving_left = False;
        self.moving_up = False;
        self.moving_down = False;
        self.speed = game_settings.hero_speed;

    def update_me(self, settings):
        # if user is pushing left, move my self.rect left etc.
        if self.moving_right:
            self.rect.centerx += 10 * settings.hero_speed;
        elif self.moving_left:
            self.rect.centerx -= 10 * settings.hero_speed;

        if self.moving_up:
            self.rect.centery -= 10 * settings.hero_speed;
        elif self.moving_down:
            self.rect.centery += 10 * settings.hero_speed;

    def draw_me(self):
        self.screen.blit(source = self.image, dest = self.rect);
