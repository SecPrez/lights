import math

LENGTH_BETWEEN_LIGHTS = 2.5
NUM_OF_LIGHTS = 500
TOTAL_LENGTH_OF_LIGHT = LENGTH_BETWEEN_LIGHTS * NUM_OF_LIGHTS
ARM_LENGTH = 38
DEGREES = 45
SPACE_BETWEEN_WIRES = 2
def calculate_length_of_wire(space_between_rows):
    position_down_arm = 0
    sum_length_of_wire = 0
    while position_down_arm < ARM_LENGTH:
        sum_length_of_wire += (2 * math.pi * math.sin(DEGREES*math.pi/180) * position_down_arm)
        position_down_arm += space_between_rows

    return sum_length_of_wire

def calculate_length_of_arm():
    position_down_arm = 0
    sum_length_of_wire = 0
    while sum_length_of_wire < (TOTAL_LENGTH_OF_LIGHT- position_down_arm):
        sum_length_of_wire += (2 * math.pi * math.sin(DEGREES*math.pi/180) * position_down_arm)
        position_down_arm += space_between_rows

    return position_down_arm

STEP_UP = 0.01
space_between_rows = 1
sum_length_of_wire = 10000
while sum_length_of_wire > TOTAL_LENGTH_OF_LIGHT:
    sum_length_of_wire = calculate_length_of_wire(space_between_rows)
    space_between_rows += STEP_UP
print("Space between rows is: " + str(space_between_rows) + " inches")

arm_length = calculate_length_of_arm()
print("Arm length is: " + str(arm_length) + " inches")

