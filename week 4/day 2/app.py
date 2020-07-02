# The first half is just boiler-plate stuff...

import pygame
import math
import random

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

# The rest is code where you implement your game using the Scenes model

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))

class GamePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Food:
    def __init__(self,location):
        self.location = location
        self.color = (100, 100, 200)
    def draw(self, screen):
        pygame.draw.rect(
            screen, 
            self.color, 
            pygame.Rect(
                self.location.x,
                self.location.y,
                10,
                10
            )
        )


class Snake:
    def __init__(self, head):
        self.body = []
        self.body.append(head)
        self.color = (200, 200, 200)
        self.dx = 10
        self.dy = 0

    def saveNewDirection(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def updateSnakePosition(self):
        newHeadPosition = GamePoint(self.body[0].x + self.dx, self.body[0].y + self.dy)
        
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x = newHeadPosition.x
        self.body[0].y = newHeadPosition.y


    def distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def canEatFood(self, food):
        if self.distance(self.body[0], food.location) < 2:
            return True
    
    def increase(self, point):
        tail = self.body[len(self.body) - 1]
        newTail = GamePoint(tail.x - 10, tail.y)
        self.body.append(newTail)

    def draw(self, screen):
        for i in range(0, len(self.body), 1):
            pygame.draw.rect(
                screen, 
                self.color, 
                pygame.Rect(
                    self.body[i].x,
                    self.body[i].y,
                    10,
                    10
                )
            )

    def printStatus(self, screen):
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("length: {}".format(len(self.body)), True, (0, 255, 255))
        screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.snake = Snake(GamePoint(50, 50))
        self.food = Food(GamePoint(30, 140))
    
    def ProcessInput(self, events, pressed_keys):
        if pressed_keys[pygame.K_UP]: 
            self.snake.saveNewDirection(0, -10)
        elif pressed_keys[pygame.K_DOWN]:
            self.snake.saveNewDirection(0, 10)
        elif pressed_keys[pygame.K_LEFT]: 
            self.snake.saveNewDirection(-10, 0)
        elif pressed_keys[pygame.K_RIGHT]:
            self.snake.saveNewDirection(10, 0)
        
    def Update(self):
        self.snake.updateSnakePosition()
        if self.snake.canEatFood(self.food):
            self.snake.increase(self.food.location)
            self.food = Food(GamePoint(random.randrange(30) * 10, random.randrange(30) * 10))
       
    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))

        for i in range(0, 300, 10):
            pygame.draw.line(screen, (0, 0, 0), (0, i), (400, i), 1)

        for i in range(0, 400, 10):
            pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 300), 1)
            


        self.snake.draw(screen)
        self.food.draw(screen)
        #self.snake.printStatus(screen)
        
        


run_game(400, 300, 60, TitleScene())