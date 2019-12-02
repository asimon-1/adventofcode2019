import glob
import sys
from os.path import join


def get_input(directory, base=sys.argv[0].split(".")[0] + ".*"):
    """Return the input as read from the given directory.

    Arguments:
        directory {str} -- The directory that contains the given file

    Keyword Arguments:
        base {str} -- The base filename, without extension (default: {sys.argv[0][:-2]+"*"})

    Returns:
        str -- The contents of the file

    """
    path = join(directory, base)
    try:
        filename = glob.glob(path)[0]
    except IndexError:
        raise FileNotFoundError(path)
    with open(filename, "r") as f:
        return f.read()


def run_main(main):
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
