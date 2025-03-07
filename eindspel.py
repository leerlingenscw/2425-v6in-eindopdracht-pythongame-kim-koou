import pygame, sys

from pygame.locals import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FPS = 10
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60
STAR_WIDTH = 60
STAR_HEIGHT = 60
EXIT_WIDTH = 60
EXIT_HEIGHT = 60
FLOWER_WIDTH = 60
FLOWER_HEIGHT = 60
WALKER_WIDTH = 60
WALKER_HEIGHT = 60
WALKER_MOVE_DELAY = 10
walker_move_counter = 0
TILE_SIZE = 60
score = 0
level = 1
MAXLEVEL = 2
MAXSTARS = 30

IMAGESDICT = {'title': pygame.image.load("title.png"),
              'story': pygame.image.load("story.png"),
              'end': pygame.image.load("end.png"),
              'fail': pygame.image.load("fail.png"),
              'hidden': pygame.image.load("hidden.png")}

class Player_1_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Player_1_1, self).__init__()
        self.x = 2 * TILE_SIZE - PLAYER_WIDTH / 2
        self.y = 2 * TILE_SIZE - PLAYER_HEIGHT / 2
        self.surf = pygame.image.load("player.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = 60

    def update(self, pressed_keys):
        new_x, new_y = self.rect.x, self.rect.y 

        if pressed_keys[K_UP] or pressed_keys[K_w]:
            new_y -= self.speed
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            new_y += self.speed
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            new_x -= self.speed
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            new_x += self.speed

        if not check_collision_1(new_x, new_y):
            self.rect.x = new_x
            self.rect.y = new_y

def check_collision_1(new_x, new_y):
    row = new_y // TILE_SIZE  
    col = new_x // TILE_SIZE  
    if 0 <= row < len(maze1) and 0 <= col < len(maze1[row]):
        return maze1[row][col] == "x"  
    return False

class Player_1_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player_1_2, self).__init__()
        self.x = 2 * TILE_SIZE - PLAYER_WIDTH / 2
        self.y = 9 * TILE_SIZE - PLAYER_HEIGHT / 2
        self.surf = pygame.image.load("player.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = 60

    def update(self, pressed_keys):
        new_x, new_y = self.rect.x, self.rect.y 

        if pressed_keys[K_UP]:
            new_y -= self.speed
        if pressed_keys[K_DOWN]:
            new_y += self.speed
        if pressed_keys[K_LEFT]:
            new_x -= self.speed
        if pressed_keys[K_RIGHT]:
            new_x += self.speed

        if not check_collision_2(new_x, new_y):
            self.rect.x = new_x
            self.rect.y = new_y

def check_collision_2(new_x, new_y):
    row = new_y // TILE_SIZE  
    col = new_x // TILE_SIZE  
    if 0 <= row < len(maze2) and 0 <= col < len(maze2[row]):
        return maze2[row][col] == "x"  
    return False

class Player_1_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Player_1_hidden, self).__init__()
        self.x = 2 * TILE_SIZE - PLAYER_WIDTH / 2
        self.y = 8 * TILE_SIZE - PLAYER_HEIGHT / 2
        self.surf = pygame.image.load("player.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = 60

    def update(self, pressed_keys):
        new_x, new_y = self.rect.x, self.rect.y 

        if pressed_keys[K_UP]:
            new_y -= self.speed
        if pressed_keys[K_DOWN]:
            new_y += self.speed
        if pressed_keys[K_LEFT]:
            new_x -= self.speed
        if pressed_keys[K_RIGHT]:
            new_x += self.speed

        if not check_collision_hidden(new_x, new_y):
            self.rect.x = new_x
            self.rect.y = new_y

def check_collision_hidden(new_x, new_y):
    row = new_y // TILE_SIZE  
    col = new_x // TILE_SIZE  
    if 0 <= row < len(mazehid) and 0 <= col < len(mazehid[row]):
        return mazehid[row][col] == "x"  
    return False

class Walker_1_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_1_1, self).__init__()
        self.x = 6 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 4 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.x += self.speed
            if self.rect.x <= self.x - WALKER_WIDTH or self.rect.x >= self.x + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_2_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_2_1, self).__init__()
        self.x = 18 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 4 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.x += self.speed
            if self.rect.x <= self.x - WALKER_WIDTH or self.rect.x >= self.x + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_3_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_3_1, self).__init__()
        self.x = 18 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 6 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.x += self.speed
            if self.rect.x <= self.x - WALKER_WIDTH or self.rect.x >= self.x + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_4_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_4_1, self).__init__()
        self.x = 18 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 8 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.x += self.speed
            if self.rect.x <= self.x - WALKER_WIDTH or self.rect.x >= self.x + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_1_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_1_2, self).__init__()
        self.x = 4 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 4 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.x += self.speed
            if self.rect.x <= self.x - WALKER_WIDTH or self.rect.x >= self.x + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_2_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_2_2, self).__init__()
        self.x = 7 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 3 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.y += self.speed
            if self.rect.y <= self.y - WALKER_WIDTH or self.rect.y >= self.y + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_3_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_3_2, self).__init__()
        self.x = 11 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 3 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.y += self.speed
            if self.rect.y <= self.y - WALKER_WIDTH or self.rect.y >= self.y + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_4_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_4_2, self).__init__()
        self.x = 18 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 3 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.x += self.speed
            if self.rect.x <= self.x - WALKER_WIDTH or self.rect.x >= self.x + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_5_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_5_2, self).__init__()
        self.x = 19 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 5 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.y += self.speed
            if self.rect.y <= self.y - WALKER_WIDTH or self.rect.y >= self.y + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_6_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_6_2, self).__init__()
        self.x = 15 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 6 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.y += self.speed
            if self.rect.y <= self.y - WALKER_WIDTH or self.rect.y >= self.y + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_7_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_7_2, self).__init__()
        self.x = 18 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 7 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.x += self.speed
            if self.rect.x <= self.x - WALKER_WIDTH or self.rect.x >= self.x + WALKER_WIDTH / 2:
                self.speed *= -1

class Walker_8_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Walker_8_2, self).__init__()
        self.x = 10 * TILE_SIZE - WALKER_WIDTH / 2
        self.y = 9 * TILE_SIZE - WALKER_HEIGHT / 2
        self.surf = pygame.image.load("walker.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (WALKER_WIDTH, WALKER_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )
        self.speed = -60
    
    def update(self, walker_move_counter):
        if walker_move_counter % WALKER_MOVE_DELAY == 0:
            self.rect.x += self.speed
            if self.rect.x <= self.x - WALKER_WIDTH or self.rect.x >= self.x + WALKER_WIDTH / 2:
                self.speed *= -1

class Trap_1_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_1_1, self).__init__()
        self.x = 2 * TILE_SIZE - TILE_SIZE / 2
        self.y = 3 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_2_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_2_1, self).__init__()
        self.x = 12 * TILE_SIZE - TILE_SIZE / 2
        self.y = 3 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_3_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_3_1, self).__init__()
        self.x = 17 * TILE_SIZE - TILE_SIZE / 2
        self.y = 3 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_4_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_4_1, self).__init__()
        self.x = 19 * TILE_SIZE - TILE_SIZE / 2
        self.y = 5 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_5_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_5_1, self).__init__()
        self.x = 17 * TILE_SIZE - TILE_SIZE / 2
        self.y = 7 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_6_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_6_1, self).__init__()
        self.x = 8 * TILE_SIZE - TILE_SIZE / 2
        self.y = 7 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_7_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_7_1, self).__init__()
        self.x = 11 * TILE_SIZE - TILE_SIZE / 2
        self.y = 9 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_8_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_8_1, self).__init__()
        self.x = 12 * TILE_SIZE - TILE_SIZE / 2
        self.y = 6 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_1_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_1_2, self).__init__()
        self.x = 3 * TILE_SIZE - TILE_SIZE / 2
        self.y = 7 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_2_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_2_2, self).__init__()
        self.x = 5 * TILE_SIZE - TILE_SIZE / 2
        self.y = 6 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_3_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_3_2, self).__init__()
        self.x = 6 * TILE_SIZE - TILE_SIZE / 2
        self.y = 9 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_4_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_4_2, self).__init__()
        self.x = 7 * TILE_SIZE - TILE_SIZE / 2
        self.y = 5 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_5_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_5_2, self).__init__()
        self.x = 9 * TILE_SIZE - TILE_SIZE / 2
        self.y = 3 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_6_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_6_2, self).__init__()
        self.x = 9 * TILE_SIZE - TILE_SIZE / 2
        self.y = 6 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_7_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_7_2, self).__init__()
        self.x = 11 * TILE_SIZE - TILE_SIZE / 2
        self.y = 6 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_8_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_8_2, self).__init__()
        self.x = 13 * TILE_SIZE - TILE_SIZE / 2
        self.y = 4 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_9_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_9_2, self).__init__()
        self.x = 13 * TILE_SIZE - TILE_SIZE / 2
        self.y = 7 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_10_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_10_2, self).__init__()
        self.x = 15 * TILE_SIZE - TILE_SIZE / 2
        self.y = 4 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Trap_11_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Trap_11_2, self).__init__()
        self.x = 17 * TILE_SIZE - TILE_SIZE / 2
        self.y = 8 * TILE_SIZE - TILE_SIZE / 2
        self.surf = pygame.image.load("trap.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE, TILE_SIZE))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_1_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_1_1, self).__init__()
        self.x = 4 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 6 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_2_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_2_1, self).__init__()
        self.x = 13 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 8 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_3_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_3_1, self).__init__()
        self.x = 15 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 9 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_1_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_1_2, self).__init__()
        self.x = 4 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 6 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_2_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_2_2, self).__init__()
        self.x = 12 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 6 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_3_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_3_2, self).__init__()
        self.x = 19 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 2 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_1_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_1_hidden, self).__init__()
        self.x = 2 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 9 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_2_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_2_hidden, self).__init__()
        self.x = 4 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 9 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_3_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_3_hidden, self).__init__()
        self.x = 4 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 6 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_4_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_4_hidden, self).__init__()
        self.x = 2 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 6 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_5_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_5_hidden, self).__init__()
        self.x = 2 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 2 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_6_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_6_hidden, self).__init__()
        self.x = 4 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 2 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_7_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_7_hidden, self).__init__()
        self.x = 4 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 4 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_8_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_8_hidden, self).__init__()
        self.x = 6 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 4 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_9_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_9_hidden, self).__init__()
        self.x = 6 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 2 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_10_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_10_hidden, self).__init__()
        self.x = 17 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 2 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_11_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_11_hidden, self).__init__()
        self.x = 17 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 7 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_12_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_12_hidden, self).__init__()
        self.x = 15 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 7 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_13_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_13_hidden, self).__init__()
        self.x = 15 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 4 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_14_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_14_hidden, self).__init__()
        self.x = 8 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 4 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_15_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_15_hidden, self).__init__()
        self.x = 8 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 6 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_16_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_16_hidden, self).__init__()
        self.x = 6 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 6 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_17_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_17_hidden, self).__init__()
        self.x = 6 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 9 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_18_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_18_hidden, self).__init__()
        self.x = 8 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 9 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_19_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_19_hidden, self).__init__()
        self.x = 8 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 8 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_20_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_20_hidden, self).__init__()
        self.x = 10 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 8 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_21_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_21_hidden, self).__init__()
        self.x = 10 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 6 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_22_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_22_hidden, self).__init__()
        self.x = 12 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 6 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_23_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_23_hidden, self).__init__()
        self.x = 12 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 9 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Star_24_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Star_24_hidden, self).__init__()
        self.x = 19 * TILE_SIZE - STAR_WIDTH / 2
        self.y = 9 * TILE_SIZE - STAR_HEIGHT / 2
        self.surf = pygame.image.load("star.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (STAR_WIDTH, STAR_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Exit_1_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Exit_1_1, self).__init__()
        self.x = 2 * TILE_SIZE - EXIT_WIDTH / 2
        self.y = 9 * TILE_SIZE - EXIT_HEIGHT / 2
        self.surf = pygame.image.load("exit.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (EXIT_WIDTH, EXIT_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Exit_1_hidden(pygame.sprite.Sprite):
    def __init__(self):
        super(Exit_1_hidden, self).__init__()
        self.x = 19 * TILE_SIZE - EXIT_WIDTH / 2
        self.y = 2 * TILE_SIZE - EXIT_HEIGHT / 2
        self.surf = pygame.image.load("exit.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (EXIT_WIDTH, EXIT_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Flower_1_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Flower_1_2, self).__init__()
        self.x = 19 * TILE_SIZE - EXIT_WIDTH / 2
        self.y = 9 * TILE_SIZE - EXIT_HEIGHT / 2
        self.surf = pygame.image.load("flower.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (EXIT_WIDTH, EXIT_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

class Hidden_1_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Hidden_1_1, self).__init__()
        self.x = 2 * TILE_SIZE - EXIT_WIDTH / 2
        self.y = 8 * TILE_SIZE - EXIT_HEIGHT / 2
        self.surf = pygame.image.load("empty.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (EXIT_WIDTH, EXIT_HEIGHT))
        self.rect = self.surf.get_rect(
            center=(
                self.x,
                self.y
            )
        )

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lava Maze')
clock = pygame.time.Clock()

LAVA_IMAGE = pygame.image.load("lava.png").convert()
LAVA_IMAGE = pygame.transform.scale(LAVA_IMAGE, (TILE_SIZE, TILE_SIZE))
FLOOR_IMAGE = pygame.image.load("floor.png").convert()
FLOOR_IMAGE = pygame.transform.scale(FLOOR_IMAGE, (TILE_SIZE, TILE_SIZE))

def draw_maze_1():
    for row_index, row in enumerate(maze1):
        for col_index, cell in enumerate(row):
            x, y = col_index * TILE_SIZE, row_index * TILE_SIZE
            if cell == "x":
                screen.blit(LAVA_IMAGE, (x, y))
            elif cell == "o":
                screen.blit(FLOOR_IMAGE, (x, y))

maze1 = [
    "xxxxxxxxxxxxxxxxxxxx",
    "xooooooooxoooxooooox",
    "xoxxxoxxoooooooxooox",
    "xoxxoooxoxxxoxxxooox",
    "xoxxxoxoooxoooxxooox",
    "xoxoooxoxoooxoxxooox",
    "xoxxxxxoxoxoooxxooox",
    "xoxoooxoxoxxoxxxooox",
    "xoooxooooooxxxooooox",
    "xxxxxxxxxxxxxxxxxxxx"
]

def draw_maze_2():
    for row_index, row in enumerate(maze2):
        for col_index, cell in enumerate(row):
            x, y = col_index * TILE_SIZE, row_index * TILE_SIZE
            if cell == "x":
                screen.blit(LAVA_IMAGE, (x, y))
            elif cell == "o":
                screen.blit(FLOOR_IMAGE, (x, y))

maze2 = [
    "xxxxxxxxxxxxxxxxxxxx",
    "xxoooxoooxoooxoooxox",
    "xooxoooxoooxoooxooox",
    "xxoooxoooxoooxoooxox",
    "xooxoooxoooxoooxooox",
    "xxoooxoooxoooxoooxox",
    "xooxoooxoooxoooxooox",
    "xxoooxoooxoooxoooxox",
    "xooxoooxoooxoooxooox",
    "xxxxxxxxxxxxxxxxxxxx"
]

def draw_maze_hidden():
    for row_index, row in enumerate(mazehid):
        for col_index, cell in enumerate(row):
            x, y = col_index * TILE_SIZE, row_index * TILE_SIZE
            if cell == "x":
                screen.blit(LAVA_IMAGE, (x, y))
            elif cell == "o":
                screen.blit(FLOOR_IMAGE, (x, y))

mazehid = [
    "xxxxxxxxxxxxxxxxxxxx",
    "xoooxooooooooooooxox",
    "xoxoxoxxxxxxxxxxoxox",
    "xoxoooxooooooooxoxox",
    "xoxxxxxoxxxxxxoxoxox",
    "xoooxoooxoooxxoxoxox",
    "xxxoxoxxxoxoxxoooxox",
    "xoxoxoxoooxoxxxxxxox",
    "xoooxoooxxxoooooooox",
    "xxxxxxxxxxxxxxxxxxxx"
]

def draw_text(score, level):
    FONT = pygame.font.Font("game_font.ttf", 64)
    textSurf = FONT.render(' STARS: ' + str(score) + '  LEVEL: ' + str(level) + '/' + str(MAXLEVEL), 1, (0, 0, 0))
    textRect = textSurf.get_rect()
    screen.blit(textSurf, textRect)

def draw_text_hidden(score):
    FONT = pygame.font.Font("game_font.ttf", 64)
    textSurf = FONT.render(' STARS: ' + str(score) + '  HIDDEN LEVEL', 1, (0, 0, 0))
    textRect = textSurf.get_rect()
    screen.blit(textSurf, textRect)

player_Lvl1 = Player_1_1()
player_Lvl2 = Player_1_2()
player_Lvlhid = Player_1_hidden()
walker1_Lvl1 = Walker_1_1()
walker2_Lvl1 = Walker_2_1()
walker3_Lvl1 = Walker_3_1()
walker4_Lvl1 = Walker_4_1()
walker1_Lvl2 = Walker_1_2()
walker2_Lvl2 = Walker_2_2()
walker3_Lvl2 = Walker_3_2()
walker4_Lvl2 = Walker_4_2()
walker5_Lvl2 = Walker_5_2()
walker6_Lvl2 = Walker_6_2()
walker7_Lvl2 = Walker_7_2()
walker8_Lvl2 = Walker_8_2()
star1_Lvl1 = Star_1_1()
star2_Lvl1 = Star_2_1()
star3_Lvl1 = Star_3_1()
star1_Lvl2 = Star_1_2()
star2_Lvl2 = Star_2_2()
star3_Lvl2 = Star_3_2()
star1_Lvlhid = Star_1_hidden()
star2_Lvlhid = Star_2_hidden()
star3_Lvlhid = Star_3_hidden()
star4_Lvlhid = Star_4_hidden()
star5_Lvlhid = Star_5_hidden()
star6_Lvlhid = Star_6_hidden()
star7_Lvlhid = Star_7_hidden()
star8_Lvlhid = Star_8_hidden()
star9_Lvlhid = Star_9_hidden()
star10_Lvlhid = Star_10_hidden()
star11_Lvlhid = Star_11_hidden()
star12_Lvlhid = Star_12_hidden()
star13_Lvlhid = Star_13_hidden()
star14_Lvlhid = Star_14_hidden()
star15_Lvlhid = Star_15_hidden()
star16_Lvlhid = Star_16_hidden()
star17_Lvlhid = Star_17_hidden()
star18_Lvlhid = Star_18_hidden()
star19_Lvlhid = Star_19_hidden()
star20_Lvlhid = Star_20_hidden()
star21_Lvlhid = Star_21_hidden()
star22_Lvlhid = Star_22_hidden()
star23_Lvlhid = Star_23_hidden()
star24_Lvlhid = Star_24_hidden()
exit_Lvl1 = Exit_1_1()
exit_Lvlhid = Exit_1_hidden()
flower_Lvl2 = Flower_1_2()
trap1_Lvl1 = Trap_1_1()
trap2_Lvl1 = Trap_2_1()
trap3_Lvl1 = Trap_3_1()
trap4_Lvl1 = Trap_4_1()
trap5_Lvl1 = Trap_5_1()
trap6_Lvl1 = Trap_6_1()
trap7_Lvl1 = Trap_7_1()
trap8_Lvl1 = Trap_8_1()
trap1_Lvl2 = Trap_1_2()
trap2_Lvl2 = Trap_2_2()
trap3_Lvl2 = Trap_3_2()
trap4_Lvl2 = Trap_4_2()
trap5_Lvl2 = Trap_5_2()
trap6_Lvl2 = Trap_6_2()
trap7_Lvl2 = Trap_7_2()
trap8_Lvl2 = Trap_8_2()
trap9_Lvl2 = Trap_9_2()
trap10_Lvl2 = Trap_10_2()
trap11_Lvl2 = Trap_11_2()
hidden_Lvl1 = Hidden_1_1()

enemies_Lvl1 = pygame.sprite.Group()
enemies_Lvl1.add(walker1_Lvl1, walker2_Lvl1, walker3_Lvl1, walker4_Lvl1, trap1_Lvl1, trap2_Lvl1, trap3_Lvl1, trap4_Lvl1, trap5_Lvl1, trap6_Lvl1, trap7_Lvl1, trap8_Lvl1)
walkers_Lvl1 = pygame.sprite.Group()
walkers_Lvl1.add(walker1_Lvl1, walker2_Lvl1, walker3_Lvl1, walker4_Lvl1)
stars1_Lvl1 = pygame.sprite.Group()
stars1_Lvl1.add(star1_Lvl1)
stars2_Lvl1 = pygame.sprite.Group()
stars2_Lvl1.add(star2_Lvl1)
stars3_Lvl1 = pygame.sprite.Group()
stars3_Lvl1.add(star3_Lvl1)
exits_Lvl1 = pygame.sprite.Group()
exits_Lvl1.add(exit_Lvl1)
hiddens_Lvl1 = pygame.sprite.Group()
hiddens_Lvl1.add(hidden_Lvl1)
all_sprites_Lvl1 = pygame.sprite.Group()
all_sprites_Lvl1.add(player_Lvl1, star1_Lvl1, star2_Lvl1, star3_Lvl1, exit_Lvl1, hidden_Lvl1, walker1_Lvl1, walker2_Lvl1, walker3_Lvl1, walker4_Lvl1, trap1_Lvl1, trap2_Lvl1, trap3_Lvl1, trap4_Lvl1, trap5_Lvl1, trap6_Lvl1, trap7_Lvl1, trap8_Lvl1)
enemies_Lvl2 = pygame.sprite.Group()
enemies_Lvl2.add(walker1_Lvl2, walker2_Lvl2, walker3_Lvl2, walker4_Lvl2, walker5_Lvl2, walker6_Lvl2, walker7_Lvl2, walker8_Lvl2, trap1_Lvl2, trap2_Lvl2, trap3_Lvl2, trap4_Lvl2, trap5_Lvl2, trap6_Lvl2, trap7_Lvl2, trap8_Lvl2, trap9_Lvl2, trap10_Lvl2, trap11_Lvl2)
walkers_Lvl2 = pygame.sprite.Group()
walkers_Lvl2.add(walker1_Lvl2, walker2_Lvl2, walker3_Lvl2, walker4_Lvl2, walker5_Lvl2, walker6_Lvl2, walker7_Lvl2, walker8_Lvl2)
stars1_Lvl2 = pygame.sprite.Group()
stars1_Lvl2.add(star1_Lvl2)
stars2_Lvl2 = pygame.sprite.Group()
stars2_Lvl2.add(star2_Lvl2)
stars3_Lvl2 = pygame.sprite.Group()
stars3_Lvl2.add(star3_Lvl2)
flowers_Lvl2 = pygame.sprite.Group()
flowers_Lvl2.add(flower_Lvl2)
all_sprites_Lvl2 = pygame.sprite.Group()
all_sprites_Lvl2.add(player_Lvl2, star1_Lvl2, star2_Lvl2, star3_Lvl2, flower_Lvl2, walker1_Lvl2, walker2_Lvl2, walker3_Lvl2, walker4_Lvl2, walker5_Lvl2, walker6_Lvl2, walker7_Lvl2, walker8_Lvl2, trap1_Lvl2, trap2_Lvl2, trap3_Lvl2, trap4_Lvl2, trap5_Lvl2, trap6_Lvl2, trap7_Lvl2, trap8_Lvl2, trap9_Lvl2, trap10_Lvl2, trap11_Lvl2)
stars1_Lvlhid = pygame.sprite.Group()
stars1_Lvlhid.add(star1_Lvlhid)
stars2_Lvlhid = pygame.sprite.Group()
stars2_Lvlhid.add(star2_Lvlhid)
stars3_Lvlhid = pygame.sprite.Group()
stars3_Lvlhid.add(star3_Lvlhid)
stars4_Lvlhid = pygame.sprite.Group()
stars4_Lvlhid.add(star4_Lvlhid)
stars5_Lvlhid = pygame.sprite.Group()
stars5_Lvlhid.add(star5_Lvlhid)
stars6_Lvlhid = pygame.sprite.Group()
stars6_Lvlhid.add(star6_Lvlhid)
stars7_Lvlhid = pygame.sprite.Group()
stars7_Lvlhid.add(star7_Lvlhid)
stars8_Lvlhid = pygame.sprite.Group()
stars8_Lvlhid.add(star8_Lvlhid)
stars9_Lvlhid = pygame.sprite.Group()
stars9_Lvlhid.add(star9_Lvlhid)
stars10_Lvlhid = pygame.sprite.Group()
stars10_Lvlhid.add(star10_Lvlhid)
stars11_Lvlhid = pygame.sprite.Group()
stars11_Lvlhid.add(star11_Lvlhid)
stars12_Lvlhid = pygame.sprite.Group()
stars12_Lvlhid.add(star12_Lvlhid)
stars13_Lvlhid = pygame.sprite.Group()
stars13_Lvlhid.add(star13_Lvlhid)
stars14_Lvlhid = pygame.sprite.Group()
stars14_Lvlhid.add(star14_Lvlhid)
stars15_Lvlhid = pygame.sprite.Group()
stars15_Lvlhid.add(star15_Lvlhid)
stars16_Lvlhid = pygame.sprite.Group()
stars16_Lvlhid.add(star16_Lvlhid)
stars17_Lvlhid = pygame.sprite.Group()
stars17_Lvlhid.add(star17_Lvlhid)
stars18_Lvlhid = pygame.sprite.Group()
stars18_Lvlhid.add(star18_Lvlhid)
stars19_Lvlhid = pygame.sprite.Group()
stars19_Lvlhid.add(star19_Lvlhid)
stars20_Lvlhid = pygame.sprite.Group()
stars20_Lvlhid.add(star20_Lvlhid)
stars21_Lvlhid = pygame.sprite.Group()
stars21_Lvlhid.add(star21_Lvlhid)
stars22_Lvlhid = pygame.sprite.Group()
stars22_Lvlhid.add(star22_Lvlhid)
stars23_Lvlhid = pygame.sprite.Group()
stars23_Lvlhid.add(star23_Lvlhid)
stars24_Lvlhid = pygame.sprite.Group()
stars24_Lvlhid.add(star24_Lvlhid)
exits_Lvlhid = pygame.sprite.Group()
exits_Lvlhid.add(exit_Lvlhid)
all_sprites_Lvlhid = pygame.sprite.Group()
all_sprites_Lvlhid.add(player_Lvlhid, exit_Lvlhid, star1_Lvlhid, star2_Lvlhid, star3_Lvlhid, star4_Lvlhid, star5_Lvlhid, star6_Lvlhid, star7_Lvlhid, star8_Lvlhid, star9_Lvlhid, star10_Lvlhid, star11_Lvlhid, star12_Lvlhid, star13_Lvlhid, star14_Lvlhid, star15_Lvlhid, star16_Lvlhid, star17_Lvlhid, star18_Lvlhid, star19_Lvlhid, star20_Lvlhid, star21_Lvlhid, star22_Lvlhid, star23_Lvlhid, star24_Lvlhid)

def terminate():
    pygame.quit()
    sys.exit()

def startScreen(walker_move_counter, level, score):
    titleRect = IMAGESDICT["title"].get_rect()
    screen.blit(IMAGESDICT["title"], titleRect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_SPACE:
                    storyScreen(walker_move_counter, level, score)
        pygame.display.update()

def storyScreen(walker_move_counter, level, score):
    titleRect = IMAGESDICT["story"].get_rect()
    screen.blit(IMAGESDICT["story"], titleRect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_SPACE:
                    main(walker_move_counter, level, score)
        pygame.display.update()

def succesScreen(score):
    titleRect = IMAGESDICT["end"].get_rect()
    screen.blit(IMAGESDICT["end"], titleRect)

    FONT = pygame.font.Font("game_font.ttf", 128)
    endScoreSurf = FONT.render('STARS: ' + str(score) + '/' + str(MAXSTARS), 1, (77, 109, 243))
    endScoreRect = endScoreSurf.get_rect(
        center=(
            400,
            450
        )
    )
    screen.blit(endScoreSurf, endScoreRect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
        pygame.display.update()

def failScreen():
    titleRect = IMAGESDICT["fail"].get_rect()
    screen.blit(IMAGESDICT["fail"], titleRect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_SPACE:
                    main(walker_move_counter, level, score)
        pygame.display.update()

def hiddenScreen(walker_move_counter, level, score):
    titleRect = IMAGESDICT["hidden"].get_rect()
    screen.blit(IMAGESDICT["hidden"], titleRect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_SPACE:
                    hidden_level(walker_move_counter, level, score)
        pygame.display.update()

def hidden_level(walker_move_counter, level, score):
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
            elif event.type == QUIT:
                terminate()
        
        pressed_keys = pygame.key.get_pressed()

        player_Lvlhid.update(pressed_keys)
        
        draw_maze_hidden()
        draw_text_hidden(score)

        for entity in all_sprites_Lvlhid:
            screen.blit(entity.surf, entity.rect)
        
        if pygame.sprite.spritecollideany(player_Lvlhid, stars1_Lvlhid):
            star1_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars2_Lvlhid):
            star2_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars3_Lvlhid):
            star3_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars4_Lvlhid):
            star4_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars5_Lvlhid):
            star5_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars6_Lvlhid):
            star6_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars7_Lvlhid):
            star7_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars8_Lvlhid):
            star8_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars9_Lvlhid):
            star9_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars10_Lvlhid):
            star10_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars11_Lvlhid):
            star11_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars12_Lvlhid):
            star12_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars13_Lvlhid):
            star13_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars14_Lvlhid):
            star14_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars15_Lvlhid):
            star15_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars16_Lvlhid):
            star16_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars17_Lvlhid):
            star17_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars18_Lvlhid):
            star18_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars19_Lvlhid):
            star19_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars20_Lvlhid):
            star20_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars21_Lvlhid):
            star21_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars22_Lvlhid):
            star22_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars23_Lvlhid):
            star23_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, stars24_Lvlhid):
            star24_Lvlhid.kill()
            score += 1
        elif pygame.sprite.spritecollideany(player_Lvlhid, exits_Lvlhid):
            main(walker_move_counter, level, score)

        pygame.display.flip()

        clock.tick(FPS)

def main(walker_move_counter, level, score):
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
            elif event.type == QUIT:
                terminate()
        
        walker_move_counter += 1
        pressed_keys = pygame.key.get_pressed()

        if level == 1:
            player_Lvl1.update(pressed_keys)
            walkers_Lvl1.update(walker_move_counter)
        
            draw_maze_1()
            draw_text(score, level)

            for entity in all_sprites_Lvl1:
                screen.blit(entity.surf, entity.rect)
        
            if pygame.sprite.spritecollideany(player_Lvl1, enemies_Lvl1):
                player_Lvl1.rect.x = 2 * TILE_SIZE - PLAYER_WIDTH
                player_Lvl1.rect.y = 2 * TILE_SIZE - PLAYER_HEIGHT
                failScreen()
            elif pygame.sprite.spritecollideany(player_Lvl1, stars1_Lvl1):
                star1_Lvl1.kill()
                score += 1
            elif pygame.sprite.spritecollideany(player_Lvl1, stars2_Lvl1):
                star2_Lvl1.kill()
                score += 1
            elif pygame.sprite.spritecollideany(player_Lvl1, stars3_Lvl1):
                star3_Lvl1.kill()
                score += 1
            elif pygame.sprite.spritecollideany(player_Lvl1, exits_Lvl1):
                level += 1
            elif pygame.sprite.spritecollideany(player_Lvl1, hiddens_Lvl1):
                player_Lvl1.rect.x = 19 * TILE_SIZE - PLAYER_WIDTH
                player_Lvl1.rect.y = 2 * TILE_SIZE - PLAYER_HEIGHT
                hidden_Lvl1.kill()
                hiddenScreen(walker_move_counter, level, score)
            
        elif level == 2:
            player_Lvl2.update(pressed_keys)
            walkers_Lvl2.update(walker_move_counter)
        
            draw_maze_2()
            draw_text(score, level)

            for entity in all_sprites_Lvl2:
                screen.blit(entity.surf, entity.rect)
        
            if pygame.sprite.spritecollideany(player_Lvl2, enemies_Lvl2):
                player_Lvl2.rect.x = 2 * TILE_SIZE - PLAYER_WIDTH
                player_Lvl2.rect.y = 9 * TILE_SIZE - PLAYER_HEIGHT
                failScreen()
            elif pygame.sprite.spritecollideany(player_Lvl2, stars1_Lvl2):
                star1_Lvl2.kill()
                score += 1
            elif pygame.sprite.spritecollideany(player_Lvl2, stars2_Lvl2):
                star2_Lvl2.kill()
                score += 1
            elif pygame.sprite.spritecollideany(player_Lvl2, stars3_Lvl2):
                star3_Lvl2.kill()
                score += 1
            elif pygame.sprite.spritecollideany(player_Lvl2, flowers_Lvl2):
                succesScreen(score)

        pygame.display.flip()

        clock.tick(FPS)

startScreen(walker_move_counter, level, score)