#1
import pygame
import random

pygame.init()

# Setup
HEIGHT = 600
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Assets
road = pygame.image.load("AnimatedStreet.png")
coin_i = pygame.image.load("Coin.png")
player_im = pygame.image.load("Player.png")
enemy_im = pygame.image.load("Enemy.png")

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound('coin.mp3')

# Fonts and counters
font = pygame.font.SysFont("Verdana", 30)
count = 0
COIN_THRESHOLD = 5
enemy_upgrade_level = 0

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_im
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_image = coin_i
        self.generate()

    def generate(self):
        self.weight = random.randint(1, 3)
        size = 50 * self.weight
        self.image = pygame.transform.scale(self.base_image, (size, size))
        self.rect = self.image.get_rect()
        self.speed = 5 + self.weight * 2
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super().__init__()
        self.image = enemy_im
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.top = 0
    
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.rect.left = random.randint(0, WIDTH - self.rect.width)
            self.rect.top = 0

# Create sprites
player = Player()
coin = Coin()
enemy = Enemy()

# Sprite groups for collision detection
coin_sprites = pygame.sprite.Group(coin)
enemy_sprites = pygame.sprite.Group(enemy)

# Main loop
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        player.move()
        coin.move()
        enemy.move()
    
        if pygame.sprite.spritecollideany(player, coin_sprites):
            coin_sound.play()
            count += coin.weight
            coin.generate()

            if count // COIN_THRESHOLD > enemy_upgrade_level:
                enemy_upgrade_level = count // COIN_THRESHOLD
                enemy.speed += 1

        if pygame.sprite.spritecollideany(player, enemy_sprites):
            game_over = True

    screen.blit(road, (0, 0))
    screen.blit(coin.image, coin.rect)
    screen.blit(enemy.image, enemy.rect)
    screen.blit(player.image, player.rect)

    score_text = font.render(f"Score: {count}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(over_text, ((WIDTH - over_text.get_width()) // 2, (HEIGHT - over_text.get_height()) // 2))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()



#2
import pygame
import sys
import random

pygame.init()

HEIGHT = 600
WIDTH = 600
grid_SIZE = 20 
grid_WIDTH = WIDTH // grid_SIZE
grid_HEIGHT = HEIGHT // grid_SIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

FOOD_TIMEOUT = 5000

LEVEL_UP_SCORE = 10


def drawGrid(surface):
    for y in range(0, grid_HEIGHT):
        for x in range(0, grid_WIDTH): 
            r = pygame.Rect((x * grid_SIZE, y * grid_SIZE), (grid_SIZE, grid_SIZE))
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                pygame.draw.rect(surface, (84, 194, 205), r)


class Snake(object):
    def __init__(self):
        self.length = 5
        cx, cy = WIDTH // 2, HEIGHT // 2
        self.positions = [(cx - i * grid_SIZE, cy) for i in range(self.length)]
        self.direction = RIGHT
        self.color = (17, 24, 47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + x * grid_SIZE, cur[1] + y * grid_SIZE)
        
        # Collision with wall
        if (
            new[0] < 0 or new[0] >= WIDTH or
            new[1] < 0 or new[1] >= HEIGHT or
            new in self.positions[1:]
        ):
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 5
        cx, cy = WIDTH // 2, HEIGHT // 2
        self.positions = [(cx - i * grid_SIZE, cy) for i in range(self.length)]
        self.direction = RIGHT

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_SIZE, grid_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:  
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)


class Food(object):
    def __init__(self, snake):
        self.color = (223, 163, 49)
        self.snake = snake
        self.randomize_position()

    def randomize_position(self):
        while True:
            self.position = (
                random.randint(0, grid_WIDTH - 1) * grid_SIZE,
                random.randint(0, grid_HEIGHT - 1) * grid_SIZE
            )
            if self.position not in self.snake.positions:
                break
        self.weight = random.randint(1, 3)
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_SIZE, grid_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
        font = pygame.font.SysFont("monospace", 16)
        text = font.render(str(self.weight), True, (0, 0, 0))
        text_rect = text.get_rect(center=r.center)
        surface.blit(text, text_rect)


snake = Snake()
food = Food(snake)
FPS = 5
score = 0
level = 1

myfont = pygame.font.SysFont("monospace", 16)

while True:
    snake.handle_keys()
    drawGrid(surface)
    snake.move()

    if pygame.time.get_ticks() - food.spawn_time > FOOD_TIMEOUT:
        food.randomize_position()

    if snake.get_head_position() == food.position:
        snake.length += food.weight
        score += food.weight
        food.randomize_position()

        if score // LEVEL_UP_SCORE + 1 > level:
            level += 1
            FPS += 1

    snake.draw(surface)
    food.draw(surface)

    screen.blit(surface, (0, 0))
    score_text = myfont.render("Score: {}".format(score), 1, (0, 0, 0))
    level_text = myfont.render("Level: {}".format(level), 1, (0, 0, 0))
    screen.blit(score_text, (5, 10))
    screen.blit(level_text, (WIDTH - 100, 10))

    pygame.display.flip()
    clock.tick(FPS)
    surface.fill((0, 0, 0))

#3
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shape Drawing")
clock = pygame.time.Clock()

color = (255, 255, 255)
radius = 2
shape = "line"  # Change to "circle", "rect", etc.
drawing = False
last_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                current_pos = event.pos
                if shape == "circle":
                    center = ((last_pos[0] + current_pos[0]) // 2,
                              (last_pos[1] + current_pos[1]) // 2)
                    radius_circle = max(abs(current_pos[0] - last_pos[0]) // 2,
                                        abs(current_pos[1] - last_pos[1]) // 2)
                    pygame.draw.circle(screen, color, center, radius_circle)
                elif shape == "rect":
                    rect = pygame.Rect(min(last_pos[0], current_pos[0]),
                                       min(last_pos[1], current_pos[1]),
                                       abs(current_pos[0] - last_pos[0]),
                                       abs(current_pos[1] - last_pos[1]))
                    pygame.draw.rect(screen, color, rect)
                elif shape == "line":
                    pygame.draw.line(screen, color, last_pos, current_pos, radius)
                elif shape == "square":
                    dx = current_pos[0] - last_pos[0]
                    dy = current_pos[1] - last_pos[1]
                    side = min(abs(dx), abs(dy))
                    start_x, start_y = last_pos
                    if dx >= 0 and dy >= 0:
                        rect = pygame.Rect(start_x, start_y, side, side)
                    elif dx < 0 and dy >= 0:
                        rect = pygame.Rect(start_x - side, start_y, side, side)
                    elif dx >= 0 and dy < 0:
                        rect = pygame.Rect(start_x, start_y - side, side, side)
                    else: 
                        rect = pygame.Rect(start_x - side, start_y - side, side, side)
                    pygame.draw.rect(screen, color, rect)
                elif shape == "right_triangle":
                    pygame.draw.polygon(screen, color, [last_pos, 
                                                        (current_pos[0], last_pos[1]), 
                                                        (last_pos[0], current_pos[1])])
                elif shape == "equilateral_triangle":
                    x1, y1 = last_pos
                    x2, y2 = current_pos
                    side_length = math.hypot(x2 - x1, y2 - y1)
                    mid = ((x1 + x2) / 2, (y1 + y2) / 2)
                    height = (math.sqrt(3) / 2) * side_length
                    dx, dy = x2 - x1, y2 - y1
                    perp = (-dy, dx)
                    length = math.hypot(perp[0], perp[1])
                    if length != 0:
                        perp = (perp[0] / length, perp[1] / length)
                    else:
                        perp = (0, 0)
                    third_vertex = (mid[0] + perp[0] * height, mid[1] + perp[1] * height)
                    pygame.draw.polygon(screen, color, [last_pos, current_pos, third_vertex])
                elif shape == "rhombus":
                    x1, y1 = last_pos
                    x2, y2 = current_pos
                    left = min(x1, x2)
                    right = max(x1, x2)
                    top = min(y1, y2)
                    bottom = max(y1, y2)
                    mid_top = ((left + right) / 2, top)
                    mid_bottom = ((left + right) / 2, bottom)
                    mid_left = (left, (top + bottom) / 2)
                    mid_right = (right, (top + bottom) / 2)
                    pygame.draw.polygon(screen, color, [mid_top, mid_right, mid_bottom, mid_left])
            drawing = False
            last_pos = None

        elif event.type == pygame.MOUSEMOTION:
            if drawing and shape == "line":
                mouse_pos = pygame.mouse.get_pos()
                if last_pos:
                    pygame.draw.line(screen, color, last_pos, mouse_pos, radius)
                last_pos = mouse_pos

    pygame.display.update()
    clock.tick(120)

pygame.quit()
