"""
14-8. Sideways Shooter, Final Version
Continue developing Sideways Shooter, using everything we’ve done in
this project. Add a Play button, make the game speed up at appropriate
points, and develop a scoring system. Be sure to refactor your code as
you work, and look for opportunities to customize the game beyond what
was shown in this chapter.
"""

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from rocket import Rocket
from bullet import Bullet
from enemy import Enemy

class SuperRocket:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Super Rocket!!!")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(
            self, "Play", self.screen.get_rect().centerx,
            self.screen.get_rect().centery)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.rocket.update()
                self._update_bullets()
                self._update_enemies()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.set_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_images()

            self.enemies.empty()
            self.bullets.empty()

            self._create_fleet()
            self.rocket.center_rocket()
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            self.stats.set_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            # Move the rocket up
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            # Move the rocket down
            self.rocket.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

        self._check_bullet_enemy_collisions()

    def _check_bullet_enemy_collisions(self):
        """Respond to bullet-enemy collisions."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True)

        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
            self.sb.prep_images()
            self.sb.check_high_score()

        if not self.enemies:
            # Destroy existing bullets and create a new fleet of enemies
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _rocket_hit(self):
        """Respond to the rocket being hit by an alien."""
        if self.stats.rockets_left > 0:
            # Decrement ships left
            self.stats.rockets_left -= 1
            self.sb.prep_rockets()
            # Get rid of any remaining aliens and bullets.
            self.enemies.empty()
            self.bullets.empty()
            # Create a new fleet and center ship.
            self._create_fleet()
            self.rocket.center_rocket()
            # Pause so the player can notice the collision and regroup
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _create_fleet(self):
        """Create the fleet of enemies."""
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        available_space_y = self.settings.screen_height - (2 * enemy_height)
        number_enemies_y = available_space_y // (2 * enemy_height)

        rocket_width = self.rocket.rect.width
        available_space_x = (
            self.settings.screen_width - (3 * enemy_height) - rocket_width)
        number_columns = available_space_x // (2 * enemy_width)

        # Create the fleet of enemies.
        for column_number in range(number_columns):
            for enemy_number in range(number_enemies_y):
                self._create_enemy(enemy_number, column_number)

    def _create_enemy(self, enemy_number, column_number):
        """Create an enemy and place it in the column."""
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        enemy.y = enemy_height + 2 * enemy_height * enemy_number
        enemy.rect.y = enemy.y
        enemy.rect.x = (enemy.rect.width + 2 * enemy.rect.width * column_number) + 250
        self.enemies.add(enemy)

    def _update_enemies(self):
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.enemies.update()

        if pygame.sprite.spritecollideany(self.rocket, self.enemies):
            self._rocket_hit()

        self._check_enemies_left()

    def _check_enemies_left(self):
        """Check if enemies have reached the left edge of the screen"""
        for enemy in self.enemies.sprites():
            if enemy.rect.left < 0:
                # Treat this the same as if the rocket got hit
                self._rocket_hit()
                break

    def _check_fleet_edges(self):
        """Respond appropriately if any enemies have reached an edge."""
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Advance the entire fleet and change the fleet's direction."""
        for enemy in self.enemies.sprites():
            enemy.rect.x -= self.settings.fleet_advance_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemies.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    sr = SuperRocket()
    sr.run_game()
