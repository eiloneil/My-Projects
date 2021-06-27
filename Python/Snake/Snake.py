# imports
import time
import turtle as tt
import random

wn = tt.Screen()
wn.bgcolor('black')
wn.title('Snake')

w = 800
h = 600
wn.setup(w, h)

score = 0
high_score = 0
DELAY = 0.1
delay = DELAY
dist = 30
head_speed = 0
NEW_SEGMENTS = 2
sc = tt.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("blue")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("score: 0  High score: 0", align = "center", font=("ds-digital", 24, "normal"))
# sc.fillcolor('blue')

dirs = ['up', 'down', 'left', 'right']
for dir in dirs:
    wn.register_shape(f'snake {dir}.gif')

wn.register_shape('apple.gif')
wn.register_shape('arrows.gif')

ars = tt.Turtle()
ars.shape('arrows.gif')
ars.speed(0)
ars.goto(w*(1.75/5), h*(2.2/5))
ars.penup()

class Snake(tt.Turtle):
    def __init__(self):
        tt.Turtle.__init__(self)
        self.isHead = 0
        self.speed(0)
        self.shape('square')
        self.color('green')
        self.direction = 'down'


class Head(Snake):
    def __init__(self):
        Snake.__init__(self)
        self.shape('snake down.gif')
        self.color('green')
        self.isHead = 1
        self.penup()

    def go_up(self):
        if self.direction != 'down':
            self.direction = 'up'
            self.shape('snake up.gif')
            # print('Go Up')

    def go_down(self):
        if self.direction != 'up':
            self.direction = 'down'
            self.shape('snake down.gif')
            # print('Go Down')

    def go_left(self):
        if self.direction != 'right':
            self.direction = 'left'
            self.shape('snake left.gif')
            # print('Go Left')

    def go_right(self):
        if self.direction != 'left':
            self.direction = 'right'
            self.shape('snake right.gif')
            # print('Go Right')


funcs = [Head.go_up, Head.go_down, Head.go_left, Head.go_right]
keys_dict = {}
keys = ['w', 's', 'a', 'd']
for i in range(len(dirs)):
    keys_dict[keys[i-1]] = [dirs[i-1], funcs[i-1]]

# Head
head = Head()
head.speed(head_speed)

wn.listen()
# for key in keys_dict.keys():
#     wn.onkeyrelease(keys_dict[key][1], key)

wn.onkeyrelease(head.go_up, 'w')
wn.onkeyrelease(head.go_left, 'a')
wn.onkeyrelease(head.go_right, 'd')
wn.onkeyrelease(head.go_down, 's')


# Apple
apple = Snake()
apple.shape('apple.gif')
apple.penup()
apple.speed(10)


def spawn_apple():
    # Spawn first apple randomly

    apple.hideturtle()

    rnd_h = random.choice([-1, 1])
    random_h = (rnd_h * random.randint(0, int((h - dist) / 60))) * dist

    rnd_w = random.choice([-1, 1])
    random_w = (rnd_w * random.randint(0, int((w - dist) / 60))) * dist

    apple.goto(random_w, random_h)
    apple.showturtle()

spawn_apple()


def collision_with_apple():
    return head.distance(apple) <= 20


def collision_with_wall():
    return (abs(head.xcor()) >= w/2) or (abs(head.ycor()) >= h/2)


def collision_with_segments():
    if len(segments) > 2:
        for seg in segments[2:]:
            if head.distance(seg) <= 20:
                return True
    else:
        return False


def score_clear(hscr, scr):
    sc.clear()
    sc.write(f"score: {scr}  High score: {hscr}", align="center", font=("ds-digital", 24, "normal"))


segments = []


def add_segment():
    new_seg = tt.Turtle()
    # new_seg.hideturtle()
    new_seg.speed(0)
    new_seg.shape('square')
    new_seg.color('green')
    new_seg.penup()
    # new_seg.goto(last_x_y[0], last_x_y[1])
    
    segments.append(new_seg)
    if len(segments) % 3 == 0:
        new_seg.color('yellow')
    # new_seg.showturtle()


def move_head():
    x = head.xcor()
    y = head.ycor()
    if head.direction == 'up':
        head.sety(y + dist)
    elif head.direction == 'down':
        head.sety(y - dist)
    elif head.direction == 'left':
        head.setx(x - dist)
    elif head.direction == 'right':
        head.setx(x + dist)


i = 0
seg_ind_1 = 0
seg_ind_2 = 0
while True:
    wn.update()
    last_head_cords = (head.xcor(), head.ycor())
    move_head()
    if collision_with_apple():
        spawn_apple()
        score += 10
        delay -= 0.001
        seg_ind_1 = 1

        if score > high_score:
            high_score = score

        score_clear(high_score, score)
        # print('Apple Eaten')

    # if seg_ind_1 == 1:
        if len(segments) > 0:
            add_segment()
        else:
            add_segment()

        for i in range(NEW_SEGMENTS-1):
            add_segment()

        # seg_ind_1 = 0
        # seg_ind_2 = 0

    if collision_with_wall() or collision_with_segments():
        # print('Crashed into the wall')
        time.sleep(1)
        spawn_apple()
        head.home()
        for seg in segments:
            seg.hideturtle()
        segments.clear()

        delay = DELAY
        score = 0
        score_clear(high_score, score)

    # for index in range(len(segments)-1,0,-1):
    #     x = segments[index-1].xcor()
    #     y = segments[index-1].ycor()
    #     segments[index].goto(x,y)
    #move segment 0 to head
    
    if len(segments) > 0:
#         segments[-1].color('green')
        x = last_head_cords[0]
        y = last_head_cords[1]
        segments[-1].goto(x,y)
        if len(segments) > 1:
            segments = [segments[-1]] + segments[:-1]
#         segments[-1].color('yellow')



    # for ii in range(len(segments)):
    #     i = ii * 1
    #     moving_seg = segments[i]
    #
    #     if i == 0:
    #         moving_seg.goto(last_head_cords)
    #     else:
    #         moving_seg.goto(last_cords)
    #
    #     last_cords = (moving_seg.xcor(), moving_seg.ycor())

    # if seg_ind_1 == 1:
    #     seg_ind_2 = 1

    time.sleep(delay)
    i += 1

print('DONE')

wn.mainloop()
