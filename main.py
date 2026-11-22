import os
from robot import Direction, Robot

CYAN = "\033[96m"
WHITE = "\033[97m"
os.system("")  # lets older Windows consoles show the colour codes below

print("This is a Toy Robot Simulator. The robot moves in a 5x5 grid depending on the direction it is facing.")
print("Please use the commands below:")
print(CYAN + "PLACE X,Y,F")
print(WHITE + "Put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST")
print(CYAN + "LEFT")
print(WHITE + "Turns the robot counterclockwise.")
print(CYAN + "RIGHT")
print(WHITE + "Turns the robot clockwise.")
print(CYAN + "MOVE")
print(WHITE + "Moves the robot forward depending on the direction its facing.")
print(CYAN + "REPORT")
print(WHITE + "Displays the current position and direction of the robot.")
robot = Robot()

while True:
    try:
        command = input().strip()
    except (EOFError, KeyboardInterrupt):
        break

    if command.startswith("PLACE "):
        data = command.replace("PLACE ", "").split(",")
        if len(data) == 3:
            try:
                x = int(data[0])
            except ValueError:
                print("X coordinate input error; Try a number from 0 to 4")
                continue
            try:
                y = int(data[1])
            except ValueError:
                print("Y coordinate input error; Try a number from 0 to 4")
                continue
            try:
                direction = Direction[data[2].strip()]
            except KeyError:
                print("Direction input error; Try NORTH, EAST, SOUTH OR WEST")
                continue
            robot.set_position(x, y, direction)
        else:
            print("Wrong format!")
    elif robot.is_placed():
        if command == "MOVE":
            robot.move_position()
        elif command == "LEFT":
            robot.turn_left()
        elif command == "RIGHT":
            robot.turn_right()
        elif command == "REPORT":
            robot.report_position()
    else:
        print("Robot is not placed.")
