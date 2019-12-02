from utils import get_input, run_main


def main(directory, part_2=False):
    input_text = get_input(directory)
    intcode = [int(x) for x in input_text.split(",")]
    for ind, opcode in enumerate(intcode):
        if ind % 4 == 0:
            if opcode == 1:
                # Addition
                intcode[intcode[ind + 3]] = intcode[intcode[ind + 1]] + intcode[intcode[ind + 2]]
            if opcode == 2:
                # Multiplication
                intcode[intcode[ind + 3]] = intcode[intcode[ind + 1]] * intcode[intcode[ind + 2]]
            if opcode == 99:
                # Break
                break
    return intcode[0]


if __name__ == "__main__":
    run_main(main)
