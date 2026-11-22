from enum import IntEnum

class Direction(IntEnum):
    """Direction of the robot to face"""
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Robot:
    def __init__(self):
        """Creates an object of the class Robot"""
        self._x = 0
        self._y = 0
        self._isplaced = False
        self._direction = Direction.NORTH

    def is_placed(self):
        """Checks if the robot is placed or not.
        Returns True if the robot is placed, else returns False."""
        return self._isplaced

    def set_position(self, x: int, y: int, direction: Direction):
        """Sets the robot at a position with x and y coordinates with direction NORTH, EAST, SOUTH or WEST"""
        if x >= 0 and x <= 4 and y >= 0 and y <= 4:
            self._x = x
            self._y = y
            self._direction = direction
            self._isplaced = True
        else:
            print("Out of bounds!")

    def report_position(self):
        """Displays the positions and direction of the robot"""
        print(f"Current Position: {self._x},{self._y},{self._direction.name}")

    def turn_right(self):
        """Turns the robot clockwise"""
        if self._direction == Direction.WEST:
            self._direction = Direction.NORTH
        else:
            self._direction = Direction(self._direction + 1)

    def turn_left(self):
        """Turns the robot counterclockwise"""
        if self._direction == Direction.NORTH:
            self._direction = Direction.WEST
        else:
            self._direction = Direction(self._direction - 1)

    def move_position(self):
        """Moves the robot forward depending on the direction it is facing"""
        match self._direction:
            case Direction.NORTH:
                if self._y == 4:
                    return
                self._y += 1
            case Direction.SOUTH:
                if self._y == 0:
                    return
                self._y -= 1
            case Direction.EAST:
                if self._x == 4:
                    return
                self._x += 1
            case Direction.WEST:
                if self._x == 0:
                    return
                self._x -= 1
