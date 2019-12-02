from utils import get_input, run_main
from itertools import product


def run_opcode(intcode, noun, verb):
    intcode = intcode.copy()
    pointer = 0
    opcode = intcode[pointer]

    # Replace noun and verb
    intcode[1] = noun
    intcode[2] = verb

    # Run the intcode
    while opcode != 99:
        if opcode == 1:
            # Addition
            param1 = intcode[pointer + 1]
            param2 = intcode[pointer + 2]
            param3 = intcode[pointer + 3]
            intcode[param3] = intcode[param1] + intcode[param2]
            pointer += 4
        elif opcode == 2:
            # Multiplication
            param1 = intcode[pointer + 1]
            param2 = intcode[pointer + 2]
            param3 = intcode[pointer + 3]
            intcode[param3] = intcode[param1] * intcode[param2]
            pointer += 4
        opcode = intcode[pointer]

    return intcode[0]


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)
    original_intcode = [int(x) for x in input_text.split(",")]
    if not part_2:
        if not test:
            noun = 12
            verb = 2
        else:
            noun = 9
            verb = 10
        return run_opcode(original_intcode, noun, verb)
    else:
        if not test:
            # Try every combination from (0,0) to (99,99)
            for (noun, verb) in product(range(100), range(100)):
                if run_opcode(original_intcode, noun, verb) == 19690720:
                    # Success
                    break
        else:
            noun = 12
            verb = 2
        return 100 * noun + verb


if __name__ == "__main__":
    run_main(main)
