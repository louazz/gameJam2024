from playscii import GameObject, GameManager
from playscii.input import Input
import random
from art import text2art

SPACESHIP = "        //-A-\\         \n" \
            "  ___---=======---___ \n" \
            "(=__\   /.. ..\   /__=) \n" \
            "     ---\__O__/---"

FLY = "      ____\n" \
      "     ;----""(#)\n" \
      "      '--|-|'|'\n" \
      "        /  |  |"
FLY_LEFT = '     ____\n' \
           '(#)""----;  \n' \
           "'|'|-|--'   \n" \
           '| | /'

FLY_UP = "        \n" \
         "       ._(@I@)_. \n" \
         "      .--{___}--. \n" \
         "      .-/  Y  \-.   \n" \
         "      /   |   \  \n" \
         "      \__/-\__/  "

FLY_DOWN = "        \n" \
           '    __   __   \n' \
           '   /  \-/  \ \n' \
           ' ._\   |   /_. \n' \
           ' .__\__Y__/__. \n' \
           '   _{___}_ \n' \
           '    (@I@)    \n'

FOOD = "*"
BIGFOOD = "<<<$>>>"

GAMEOVER = text2art('''Game Over''',font="small",chr_ignore=True)
N = 100

class Fly(GameObject):
    def __init__(self, pos=(40, 7)):
        super().__init__(pos=pos, render=FLY)
        self.vel = (10, 10)

    '''
     def update(self):
        self.x += self.vel[0] * self.delta_time
        
    '''


class Food(GameObject):
    def __init__(self, pos=(0, 5)):
        super().__init__(pos=pos, render=FOOD)
        self.vel = (10, 10)

    def update(self):
        self.x -= self.vel[0] * self.delta_time
        self.y += self.vel[1] * self.delta_time

class FlyManager(GameManager):
    def __init__(self):
        super().__init__((80, 40))
        self.food = [Food(pos=(random.randint(0, 80), random.randint(0, 40))),
                     Food(pos=(random.randint(0, 80), random.randint(0, 40)))
            , Food(pos=(random.randint(0, 80), random.randint(0, 40))),
                     Food(pos=(random.randint(0, 80), random.randint(0, 40)))
            , Food(pos=(random.randint(0, 80), random.randint(0, 40))),
                     Food(pos=(random.randint(0, 80), random.randint(0, 40)))
                     ]
        self.fly = Fly()
        self.set_title('This is a game ...')
        self.score =0

    def setup(self):
        for obj in self.food:
            self.add_object(obj)
        self.add_object(self.fly)

    def update(self):
        for obj in self.food:
            if obj.x <= 0 or obj.x >= 80:
                obj.vel = (-obj.vel[0], obj.vel[1])
            if obj.y <= 0 or obj.y >= 40:
                obj.vel = (obj.vel[0], -obj.vel[1])

            if self.fly.x >= obj.x -5 and self.fly.x <= obj.x +5 and self.fly.y >= obj.x - 5 and self.fly.y <= obj.x + 5:
                obj.x = 1000
                obj.y = 1000
                self.score += 1

        self.set_title(text2art(" score: "+str(self.score)+": 6", "white_bubble"))

        if self.fly.x <= 0:
            self.fly.x = 80
        if self.fly.x >= 80:
            self.fly.x = 0

        if self.fly.y >= 40:
            self.fly.y = 0

        if self.fly.y <= 0:
            self.fly.y = 40
        if Input.get_key('right'):
            self.fly.x += 20 * self.delta_time
            self.fly.render = FLY

        if Input.get_key('left'):
            self.fly.x -= 20 * self.delta_time
            self.fly.render = FLY_LEFT

        if Input.get_key('up'):
            self.fly.y += 20 * self.delta_time
            self.fly.render = FLY_UP
        if Input.get_key('down'):
            self.fly.y -= 20 * self.delta_time
            self.fly.render = FLY_DOWN

        if self.score == len(self.food):
            self.fly.x = 15
            self.fly.y = 20
            self.fly.render=GAMEOVER
            self.quit()


if __name__ == '__main__':
    space = FlyManager()
    space.start()
