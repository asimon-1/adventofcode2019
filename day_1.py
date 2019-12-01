from utils import get_input


def main(directory, part_2=False):
    input_text = get_input(directory)
    counter = 0
    for line in input_text.splitlines():
        fuel_mass = int(line) // 3 - 2
        if part_2:
            while fuel_mass > 0:
                counter += fuel_mass
                fuel_mass = fuel_mass // 3 - 2
        else:
            counter += fuel_mass
    return counter


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
