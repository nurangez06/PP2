#1
import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="masusymay2020", host="localhost", port="5432")
cur = conn.cursor()

name = input("Enter name: ")
phone = input("Enter phone: ")
cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))

conn.commit()
conn.close()



#2
import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="masusymay2020",
    port="5432"
)

cur = conn.cursor()

def insert_from_console():
    while True:
        name = input("Enter name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        phone = input("Enter phone number: ")
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print(f"{name} has been saved!\n")

def insert_from_csv():
    path = input("Enter CSV file path (e.g. contacts.csv): ")
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                            (row['name'], row['phone']))
        conn.commit()
        print("Data imported from CSV!")
    except Exception as e:
        print("Error:", e)

def update_contact():
    name = input("Enter the name to update: ")
    new_phone = input("Enter the new phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print(f"Updated phone number for {name}")

def delete_contact():
    name = input("Enter the name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    print(f"Deleted contact with name: {name}")

def show_all_contacts():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print("\nPhoneBook records:")
    for row in rows:
        print(row)

while True:
    print("\n===== PhoneBook Menu =====")
    print("1. Add contact manually")
    print("2. Import from CSV file")
    print("3. Update phone number")
    print("4. Delete contact")
    print("5. Show all contacts")
    print("0. Exit")

    choice = input("Select option: ")

    if choice == "1":
        insert_from_console()
    elif choice == "2":
        insert_from_csv()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        show_all_contacts()
    elif choice == "0":
        break
    else:
        print("Invalid choice!!!!")

cur.close()
conn.close()



#3
import pygame
import sys
import random
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="masusymay2020",
    port="5432"
)
cur = conn.cursor()

player_name = input("Enter your name: ")

cur.execute("SELECT level FROM snake_users WHERE username = %s", (player_name,))
row = cur.fetchone()
if row:
    level = row[0]
    print(f"Welcome back, {player_name}! Current level: {level}")
else:
    level = 1
    cur.execute("INSERT INTO snake_users (username, level) VALUES (%s, %s)", (player_name, level))
    conn.commit()
    print(f"Welcome, {player_name}! Starting at level 1.")

score = 0
FPS = 5 + (level - 1) * 2  

pygame.init()
HEIGHT = 600
WIDTH = 600
grid_SIZE = 20
grid_WIDTH = WIDTH // grid_SIZE
grid_HEIGHT = HEIGHT // grid_SIZE
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
FOOD_TIMEOUT = 5000

def drawGrid(surface):
    for y in range(grid_HEIGHT):
        for x in range(grid_WIDTH):
            r = pygame.Rect((x * grid_SIZE, y * grid_SIZE), (grid_SIZE, grid_SIZE))
            color = (144, 238, 144) if (x + y) % 2 == 0 else (152, 251, 152)  
            pygame.draw.rect(surface, color, r)

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * grid_SIZE)) % WIDTH), (cur[1] + (y * grid_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        global score, FPS
        cur.execute("INSERT INTO snake_scores (username, score) VALUES (%s, %s)", (player_name, score))
        conn.commit()
        print(f"\u2620\ufe0f Game over! Score saved: {player_name} — {score}")
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        score = 0
        FPS = 5 + (level - 1) * 2

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_SIZE, grid_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        global score, FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: self.turn(UP)
                elif event.key == pygame.K_DOWN: self.turn(DOWN)
                elif event.key == pygame.K_LEFT: self.turn(LEFT)
                elif event.key == pygame.K_RIGHT: self.turn(RIGHT)
                elif event.key == pygame.K_p:
                    cur.execute("INSERT INTO snake_scores (username, score) VALUES (%s, %s)", (player_name, score))
                    conn.commit()
                    print(f"\ud83d\udcbe Saved manually: {player_name} — {score}")

class Food(object):
    def __init__(self):
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_WIDTH - 1) * grid_SIZE,
                         random.randint(0, grid_HEIGHT - 1) * grid_SIZE)
        self.weight = random.randint(1, 3)
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_SIZE, grid_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
        font = pygame.font.SysFont("monospace", 16)
        text = font.render(str(self.weight), True, (0, 0, 0))
        surface.blit(text, text.get_rect(center=r.center))

snake = Snake()
food = Food()
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
        FPS += food.weight
        food.randomize_position()

    snake.draw(surface)
    food.draw(surface)

    screen.blit(surface, (0, 0))
    text = myfont.render("Score: {0}".format(score), 1, (0, 0, 0))
    screen.blit(text, (5, 10))

    pygame.display.flip()
    clock.tick(FPS)

###
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="masusymay2020"
)
cur = conn.cursor()

# Create the users table
cur.execute("""
CREATE TABLE IF NOT EXISTS snake_users (
    username VARCHAR(50) PRIMARY KEY,
    level INTEGER DEFAULT 1
)
""")

# Create the scores table
cur.execute("""
CREATE TABLE IF NOT EXISTS snake_scores (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    score INTEGER,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
cur.close()
conn.close()

print("✅ Tables created successfully!")
