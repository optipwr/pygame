import pygame;
# # we need sys to halt the program
# import sys;
# import our settings from our settings module
from settings import Settings;

from hero import Hero;
from game_functions import check_events;
from pygame.sprite import Group, groupcollide;
# get our enemy class
from enemy import Enemy;

from button import Start_Button;

# initialize all of the pygame modules
pygame.init();
# screen_size = (1000,800);
# make a background color
# bg_color = (82, 111, 53);

# Put a message on the status barplayer knows the name of the game
pygame.display.set_caption("Bunny Dump!");
# Create an object our of our settings class
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);

# Make a group for the hero to belong to so we can use groupcollide
hero_group = Group();
hero = Hero(screen, game_settings);

hero_group.add(hero);

enemies = Group();
enemies.add(Enemy(screen, game_settings));

# make a start button
start_button = Start_Button(screen);


# This loop will run forever...
while 1:
    # run our check_events here!
    check_events(hero, start_button, game_settings);
    # Put our bg color as the fill in our game
    screen.fill(game_settings.bg_color);

    for hero in hero_group.sprites():
        if game_settings.game_active:
            hero.update_me(game_settings);
        hero.draw_me();

    for enemy in enemies.sprites():
        if game_settings.game_active:
            enemy.update_me(hero);
        enemy.draw_me();

    hero_died = groupcollide(hero_group, enemies, True, False);
    if hero_died:
        print "You lost!";
        game_settings.game_active = False;

    if game_settings.game_active == False:
        start_button.draw_button();



    # flip the screen = wipe it out
    pygame.display.flip();
