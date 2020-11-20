# Get started with interactive Python
import turtle
import time
import queue
import timeit

wn = turtle.Screen()
wn.reset()
wn.setup(850,700)
wn.bgcolor("black")

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Finish(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("cyan")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 22

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            return True;

        return False;

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 22

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            return True;

        return False;

    def go_right(self):
        move_to_x = player.xcor() + 22
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            return True;

        return False;

    def go_left(self):
        move_to_x = player.xcor() - 22
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            return True;

        return False;

#create Levels list
levels = [""]

#define levels
level_1 = [
"XXXXXXXXXXXXXX",
"XPXXXXXXXXXXXX",
"X   XX       X",
"X X X  XXXXX X",
"X X XX     XXX",
"X X    XXX X F",
"X XXXX X X X X",
"X    X X   X X",
"XXXXXX XXXXX X",
"X            X",
"XXXXXXXXXXXXXX",
]

level_2 = [
"XXXXXXXXXXXXXX",
"XPXXXXXXXXXXXX",
"X   XX       X",
"X X X  XXXXX X",
"X X XX     XXX",
"X X    XXX X X",
"X XXXX X X X X",
"X    X X   X X",
"XXXXXX XXXXX X",
"X            X",
"XXXXXXXXX XXXX",
"X   XXX      X",
"X X X  XXXXX X",
"X X XX     X X",
"X X    XXX X X",
"X XXXX X X X X",
"X    X X   X X",
"XXXXXX XXXXX X",
"X        X   F",
"XXXXXXXXXXXXXX",
]

level_3 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XPXXXXXXXXXXXXXXXXXXXXXXXXX",
"X   XX       X   XX       F",
"X X X  XXXXX X X X  XXXXX X",
"X X XX     X X X XX     XXX",
"X X    XXX X X X    XXX X X",
"X XXXX X X X X XXXXXX X X X",
"X    X X   X X    X X     X",
"XXX XXXXXXXX XXXX X XXXXX X",
"X          X   X    X     X",
"XXX XXXXXXXXXXXXXX XXXX XXX",
"X   XX       X   X X      X",
"X X X  XXXXX X X X XXXXXXXX",
"X X XX     X X X X        X",
"X X    XXX X   X    XXX X X",
"X XXXX X X X X XXXX X X X X",
"X    X X   X X    X X   X X",
"XXXXXX XXXXX XXXXXX XXX XXX",
"X        X   X        X   X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

level_4 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XPXXXXXXXXXXXXXXXXXXXXXXXXX",
"X   XX       X   XX       X",
"X X X  XXXXX X X X  XXXXX X",
"X X XX     X X X XX     XXX",
"X X    XXX X X X    XXX X X",
"X XXXX X X X X XXXXXX X X X",
"X    X X   X X    X X     X",
"XXX XXXXXXXX XXXX X XXXXX X",
"X          X   X    X     X",
"XXX XXXXXXXXXXXXXX XXXX XXX",
"X   XX       X   X X      X",
"X X X  XXXXX X X X XXXXXX X",
"X X XX     X X X X      X X",
"X X    XXX X   X    XXX X X",
"X XXXX X X X X XXXX X X X X",
"X    X X   X X    X X   X F",
"XXXXXX XXXXX XXXXXX XXX XXX",
"X        X   X        X   X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

level_5 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XPXXXXXXXXXXXXXXXXFXXXXXXXX",
"X           X      X      X",
"XXXXXXXXX XXXX XXXXX XX XXX",
"X           X         X   X",
"X X XXXXX XXXXXXXXXXX XX XX",
"X X    X     X     X  X   X",
"X X XXXXXXXXXX XXX XXXXXX X",
"X X      X      X   X     X",
"X X XXX XX XXXXXX XXXXXXX X",
"X X   X X       X       X X",
"X X XXXXX XXXX XXXXXXXX X X",
"X X   X      X      X     X",
"X X XXXXXXXXXX XXXXXXX XXXX",
"X X       X    X       X  X",
"X XXX XXX X XXXXX XXXXXX XX",
"X X X X   X  X      X     X",
"XXX XXXXX X XXXXX XXXXXX XX",
"X            X            X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

level_6 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XPXXXXXXXXXXXXXXXXFXXXXXXXX",
"X           X      X      X",
"XXXXXXXXX XXXX XXXXX XX XXX",
"X           X         X   X",
"X X XXXXX XXXXXXXXXXX XX XX",
"X X    X     X     X  X   X",
"X X XXXXXXXXXX XXX XXXXXX X",
"X X      X      X   X     X",
"X X XXX XX XXXXXX XXXXXXX X",
"X X   X X       X       X X",
"XXX XXXXX XXXX XXXXXXXX X X",
"X     X      X      X   X X",
"X XXXXXXXXXXXX XXXXXXX XX X",
"X         X    X       X  X",
"X XXX XXX X XXXXX XXXXXX XX",
"X X X X   X  X      X     X",
"X X XXXXX X XXXXX XXXXXX XX",
"X     X      X            X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Add maze to mazes list
level = int(input("Select level (1-6)\n->"))
if level == 1:
    levels.append(level_1)
elif level == 2:
    levels.append(level_2)
elif level == 3:
    levels.append(level_3)
elif level == 4:
    levels.append(level_4)
elif level == 5:
    levels.append(level_5)
elif level == 6:
    levels.append(level_6)

print("\nrendering maze...\n")

#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the Character at each x,y coordinate
            #NOTE the order of the y and x in the next line
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -320 + (x * 22)
            screen_y = 200 - (y * 22)

            #Check if it is an X (representing a wall)
            if character == "X":
                if screen_y == 200:
                    pen.color("black")
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    walls.append((screen_x,screen_y))
                else:
                    pen.color("white")
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    walls.append((screen_x,screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "F":
                finish.goto(screen_x, screen_y)

#verifies if sequence of moves is valid
def valid(moves):
    player.goto(initx, inity)
    prev = ""

    for x in moves:
        if trace == "y" or trace == "Y":
            time.sleep(0.02)

        if x == "L":
            if not player.go_left() or prev == "R":
                return False
        elif x == "R":
            if not player.go_right() or prev == "L":
                return False
        elif x == "U":
            if not player.go_up() or prev == "D":
                return False
        elif x == "D":
            if not player.go_down() or prev == "U":
                return False;

        prev = x

    return True;

#check if player reached end
def final(moves):
    player.goto(initx, inity)

    for x in moves:
        if x == "U":
            player.go_up()
        elif x == "D":
            player.go_down()
        elif x == "L":
            player.go_left()
        elif x == "R":
            player.go_right()

    if player.xcor() == finish.xcor() and player.ycor() == finish.ycor():
        return True;

    return False;


#Create class instances
pen = Pen()
player = Player()
finish = Finish()

# Walls
walls=[]

#Set up the level
setup_maze(levels[1])

'''
#Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")
'''

#Turn off screen upates
trace = input("Show traces? (y/n): ")

if trace == "n" or trace == "N":
    print("\ncalculating path...\n")
    wn.tracer(0)

nums = queue.Queue()
nums.put("")
add = ""

initx = player.xcor()
inity = player.ycor()

start = timeit.default_timer()

#Main Game Loop
while True:
    add = nums.get()

    if trace == "y" or trace == "Y":
        print(add)

    for j in ["U", "R", "D", "L"]:
        if trace == "y" or trace == "Y":
            time.sleep(0.02)

        put = add + j

        if valid(put):
            nums.put(put)

        if final(put):
            stop = timeit.default_timer()

            print("path: " + put)
            print("steps: ", len(put))
            print('time: ', stop - start)

            player.goto(initx, inity)

            for x in put:
                wn.update()
                pen.goto(player.xcor(), player.ycor())
                pen.color("red")
                pen.stamp()
                time.sleep(0.1)
                if x == "U":
                    player.go_up()
                elif x == "D":
                    player.go_down()
                elif x == "L":
                    player.go_left()
                elif x == "R":
                    player.go_right()

                wn.update()

            finish.color("red")
            wn.update()
            time.sleep(1)
            wn.reset()
            turtle.color("red")
            turtle.write("YOU WON!!!\n", align= "center", font=("Arial", 60, "normal"))
            turtle.color("white")
            turtle.write("Path:  " + put + "\nSteps: %s\nTime: %.3f seconds" %(len(put),(stop - start)), align= "center", font=("Arial", 10, "normal"))
            time.sleep(3)
            exit()
