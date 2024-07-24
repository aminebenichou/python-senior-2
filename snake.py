import pygame
import random

class Food():
    x, y = random.randint(30, 1260), random.randint(30, 700)
    color = random.choice(["blue", "purple", "yellow", "red"])

    def create_food(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), 20)

    def eaten(self, player):
        if player.x < self.x+20 and player.x > self.x-20 and player.y < self.y+20 and player.y > self.y-20 :
            self.x, self.y = random.randint(30, 1260), random.randint(30, 700)
            return True
class Player():
    score = 0
    health = 100
    x = 200
    y = 200
    
    body = [(200, 200)]
    speed = 22
    def draw(self, window):
        for pos in self.body:
            pygame.draw.rect(window, 'blue', pygame.Rect(pos[0], pos[1], 20, 20))

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.body.insert(0,(self.x, self.y))
            self.body.pop()
            
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.body.insert(0,(self.x, self.y))
            self.body.pop()
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.body.insert(0,(self.x, self.y))
            self.body.pop()
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.body.insert(0,(self.x, self.y))
            self.body.pop()
    def grow(self):
        self.body.append(self.body[-1])

pygame.init()
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))
food = Food()
snake = Player()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    keys = pygame.key.get_pressed()
    window.fill('black')
    snake.move(keys)
    snake.draw(window)
    food.create_food(window)
    if food.eaten(snake) :
        snake.score += 1
        snake.grow()
        print(snake.score)
    pygame.display.flip()
    pygame.time.Clock().tick(20)



pygame.quit()






body = [(3,3), (2,2), (2,2), (1,1)]