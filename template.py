from utils import get_input


def main(directory):
    input_text = get_input(directory)
    return input_text


if __name__ == "__main__":
    expected_test = int(get_input("outputs_test"))
    answer_test = main("inputs_test")
    if expected_test == answer_test:
        print("Test input successful.")
        answer = main("inputs")
        print(f"The answer is {answer}")
    else:
        print("Test input was not successful!")
        print(f"Expected answer:\t{expected_test}")
        print(f"Calculated answer:\t{answer_test}")
