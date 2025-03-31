import os
import random
import readchar

POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 11

my_position = [3, 1]
tail_length = 0
map_objects = []
tail = []

map = """\
#############################
#   ###         ###         #
#   ###         ###         #
#   ###         ###         #
#   ###   ###   ###   ###   #
#   ###   ###   ###   ###   #
#   ###   ###   ###   ###   #
#   ###   ###   ###   ###   #
#   ###   ###   ###   ###   #
#   ###   ###   ###   ###   #
#   ###   ###   ###   ###   #
#         ###         ###   #
#         ###         ###   #
#         ###         ###   # 
#############################\
"""

end_game = False
died = False

#Creation of the map
map = [list(row) for row in map.split("\n")]

MAP_WIDTH = len(map[0])
MAP_HEIGHT = len(map)

#Main loop
while not end_game:
    os.system("clear")
    # generate randome objects
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_object = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_object not in map_objects and new_object != my_position and \
                map[new_object[POS_Y]][new_object[POS_X]] != "#":
            map_objects.append(new_object)

    #Draw map

    print(" " + "-" * MAP_WIDTH * 3 + " ")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    end_game = True
                    died = True

            if map[cordinate_y][cordinate_x] == "#":
                char_to_draw = "#"

            print(" {} " .format(char_to_draw), end="")
        print("|")

    print(" " + "-" * MAP_WIDTH * 3 + " ")

    #Ask user where he wnats to move

    #direction = input("Muevete! [WASD] ")

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        end_game = True

    if new_position:
        if map[my_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

    os.system("clear")

if died:
    print("Has muerto!")
