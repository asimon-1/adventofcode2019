from utils import get_input


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
    for ind in (0, 1):
        expected_test = int(get_input("outputs_test").splitlines()[ind])
        answer_test = main("inputs_test", ind)
        print(f"\nPart {ind+1}")
        if expected_test == answer_test:
            print("Test input successful.")
            answer = main("inputs", ind)
            print(f"The answer is {answer}")
        else:
            print("Test input was not successful!")
            print(f"Expected answer:\t{expected_test}")
            print(f"Calculated answer:\t{answer_test}")
