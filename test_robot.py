import subprocess
import sys
from pathlib import Path

def run(commands):
    """Type the commands into main.py and return what it printed after the help text."""
    result = subprocess.run([sys.executable, "main.py"],
                            input="\n".join(commands) + "\n",
                            capture_output=True, text=True,
                            cwd=Path(__file__).parent)
    lines = result.stdout.splitlines()
    return lines[12:]  # main.py prints 12 lines of help first


# TEST CASE 1: a PLACE off the table is refused
output = run(["PLACE 6,0,NORTH"])
assert output == ["Out of bounds!"], output

# TEST CASE 2: the robot stops at the edge of the table
output = run(["PLACE 3,3,EAST",
              "MOVE",
              "MOVE",
              "LEFT",
              "MOVE",
              "MOVE",
              "REPORT"])
assert output == ["Current Position: 4,4,NORTH"], output

# TEST CASE 3: turning left four times goes all the way round
output = run(["PLACE 0,0,NORTH",
              "LEFT",
              "REPORT",
              "LEFT",
              "REPORT",
              "LEFT",
              "REPORT",
              "LEFT",
              "REPORT"])
assert output == ["Current Position: 0,0,WEST",
                  "Current Position: 0,0,SOUTH",
                  "Current Position: 0,0,EAST",
                  "Current Position: 0,0,NORTH"], output

# TEST CASE 4: commands before a PLACE are refused
output = run(["MOVE"])
assert output == ["Robot is not placed."], output

# TEST CASE 5: a PLACE without all three values is refused
output = run(["PLACE 1,2"])
assert output == ["Wrong format!"], output

# TEST CASE 6: a bad value in PLACE is refused, not replaced with a default
output = run(["PLACE a,3,EAST", "REPORT"])
assert output == ["X coordinate input error; Try a number from 0 to 4",
                  "Robot is not placed."], output

output = run(["PLACE 2,2,UP", "REPORT"])
assert output == ["Direction input error; Try NORTH, EAST, SOUTH OR WEST",
                    "Robot is not placed."], output

# TEST CASE 7: surrounding spaces are ignored
output = run([" PLACE 1,2,EAST ", "MOVE ", "REPORT"])
assert output == ["Current Position: 2,2,EAST"], output

# TEST CASE 8: only a command starting with PLACE places the robot
output = run(["REPLACE 1,1,NORTH", "REPORT"])
assert output == ["Robot is not placed.", "Robot is not placed."], output 

# TEST CASE 9: an invalid PLACE leaves the robot off the table
output = run(["PLACE 9,9,NORTH", "MOVE", "REPORT"])
assert output == ["Out of bounds!", "Robot is not placed.",
                    "Robot is not placed."], output

# TEST CASE 10: the three examples from the brief
assert run(["PLACE 0,0,NORTH", "MOVE", "REPORT"]) == ["Current Position: 0,1,NORTH"]
assert run(["PLACE 0,0,NORTH", "LEFT", "REPORT"]) == ["Current Position: 0,0,WEST"]
assert run(["PLACE 1,2,EAST", "MOVE", "MOVE", "LEFT", "MOVE", "REPORT"]) == ["Current Position: 3,3,NORTH"]
 
print("All tests passed")
