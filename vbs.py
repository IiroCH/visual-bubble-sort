from turtle import *
from random import shuffle
from time import sleep, time

bg_color = '#000000'
col_color = '#FFFF00'

edge = 0.05
col_mult = 0.5

list_size = 60

screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor(bg_color)
screen.setworldcoordinates(0, 0, screen.window_width(), screen.window_height())
tracer(0)

turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)


def draw_column(height, width, index):

    turtle.teleport(edge*screen.window_width() + index*width, edge*screen.window_height())

    turtle.color(col_color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.fd(width*col_mult)
        turtle.lt(90)
        turtle.fd(height)
        turtle.lt(90)
    turtle.end_fill()

    turtle.teleport(turtle.xcor(), turtle.ycor() + height)

    turtle.color(bg_color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.fd(width*col_mult)
        turtle.lt(90)
        turtle.fd(screen.window_height() - 2 * edge - height)
        turtle.lt(90)
    turtle.end_fill()
    

def update_visual(values, pair_1=None, pair_2=None):
    

    w = (1 - 2 * edge) * screen.window_width() / len(values)
    max_h = (1 - 2 * edge) * screen.window_height()
    h_unit = max_h / max(values)

    if pair_1 == None:
        for i in range(len(values)):
            draw_column(h_unit * values[i], w, i)
    else:
        draw_column(h_unit * values[pair_1], w, pair_1)
        draw_column(h_unit * values[pair_2], w, pair_2)

    screen.update()
    #sleep(0.1)


def bubblesort(values):

    print(f"Unsorted values: {values}")
    start_time = time()
    
    check_len = len(values)
    while check_len > 1:
        new_check_len = 0
        for i in range(1, check_len):
            if values[i-1] > values[i]:
                switch = values[i-1]
                values[i-1] = values[i]
                values[i] = switch

                update_visual(values, i-1, i)

                new_check_len = i

        #update_visual(values)

        check_len = new_check_len

    end_time = time()
    print(f"Sorted values: {values}")
    print(f"Sort time: {end_time - start_time} seconds")


def main():

    values = []
    for num in range(1, list_size+1):
        values.append(num)
    shuffle(values)
    update_visual(values)

    bubblesort(values)


if __name__ == "__main__":
    main()
