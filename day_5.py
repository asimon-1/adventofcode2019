from utils import get_input, run_main
from itertools import product


def addition(intcode, param1, param2, param3, mode1, mode2, mode3):
    val1 = param1 if mode1 else intcode[param1]
    val2 = param2 if mode2 else intcode[param2]

    if mode3:
        # Immediate
        raise RuntimeError
    else:
        # Position
        intcode[param3] = val1 + val2
    return intcode


def multiplication(intcode, param1, param2, param3, mode1, mode2, mode3):
    val1 = param1 if mode1 else intcode[param1]
    val2 = param2 if mode2 else intcode[param2]
    if mode3:
        # Immediate
        raise RuntimeError
    else:
        # Position
        intcode[param3] = val1 * val2
    print(intcode)
    return intcode


def input(intcode, param1, inp):
    intcode[param1] = inp
    return intcode


def output(intcode, param1, mode1):
    return param1 if mode1 else intcode[param1]


def run_opcode(intcode, inp):
    intcode = intcode.copy()
    pointer = 0
    out = 0
    opcode = intcode[pointer]

    # Run the intcode
    while (operation := opcode % 100) != 99:
        mode1 = opcode // 10 ** 2 % 10
        mode2 = opcode // 10 ** 3 % 10
        mode3 = opcode // 10 ** 4 % 10
        if operation == 1:
            # Addition
            intcode = addition(
                intcode, intcode[pointer + 1], intcode[pointer + 2], intcode[pointer + 3], mode1, mode2, mode3,
            )
            pointer += 4
        elif operation == 2:
            # Multiplication
            intcode = multiplication(
                intcode, intcode[pointer + 1], intcode[pointer + 2], intcode[pointer + 3], mode1, mode2, mode3,
            )
            pointer += 4
        elif operation == 3:
            # Input
            intcode = input(intcode, intcode[pointer + 1], inp)
            pointer += 2
        elif operation == 4:
            # Output
            out = output(intcode, intcode[pointer + 1], mode1)
            pointer += 2

        opcode = intcode[pointer]

    return out


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)
    original_intcode = [int(x) for x in input_text.split(",")]
    if not part_2:
        return run_opcode(original_intcode, 1)
    else:
        return


if __name__ == "__main__":
    run_main(main)
