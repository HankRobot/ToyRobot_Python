# Toy Robot Simulator
A simulation of a toy robot moving on a 5 x 5 tabletop. The robot cannot fall off: any placement or move that would take it off the table is ignored, and later valid commands still work.

## Requirements
Python 3.10 or newer

## Running
In terminal, run:
python main.py

## Input Example
```
MOVE
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
PLACE 4,4,NORTH
MOVE
REPORT
```

Output:
```
Robot is not placed.
Current Position: 3,3,NORTH
Current Position: 4,4,NORTH
```

## Tests
In terminal, run:
python test_robot.py

