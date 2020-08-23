import random

onGrid = [21, 41, 81, 101, 121, 141, 161, 181, 201, 221, 241, 261, 281, 301, 321, 341, 361, 381, 401, 421, 441, 461,
          481, 501, 521, 541, 561, 581]


class Snake:
    def __init__(self, snake_x, snake_y):
        self.snake_x = snake_x
        self.snake_y = snake_y

    def getPosX(self):
        return self.snake_x

    def getPosY(self):
        return self.snake_y

    def moveUp(self):
        if not self.snake_y == 1:
            self.snake_y += 10
        return self.snake_y

    def moveDown(self):
        if not self.snake_y == 581:
            self.snake_y += 10
        return self.snake_y

    def moveRight(self):
        if not self.snake_x == 581:
            self.snake_x += 10
        return self.snake_x

    def moveLeft(self):
        if not self.snake_x == 1:
            self.snake_x += 10
        return self.snake_x


class SnakeFood:
    def __init__(self, snake_food_x, snake_food_y):
        self.snake_food_x = snake_food_x
        self.snake_food_y = snake_food_y

    def PickLocation(self):
        self.snake_food_x = random.choice(onGrid)
        self.snake_food_y = random.choice(onGrid)

    def getX(self):
        return self.snake_food_x

    def getY(self):
        return self.snake_food_y
