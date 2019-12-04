from utils import get_input, run_main
from math import log10


def check_increasing(n):
    digits = int(log10(n)) + 1
    n_digits = [n // 10 ** e % 10 for e in range(digits - 1, -1, -1)]
    if all((n_digits[i + 1] - n_digits[i] >= 0 for i in range(len(n_digits) - 1))):
        return True
    return False


def check_adjacent(n):
    digits = int(log10(n)) + 1
    n_digits = [n // 10 ** e % 10 for e in range(digits - 1, -1, -1)]
    if any((n_digits[i + 1] == n_digits[i] for i in range(len(n_digits) - 1))):
        return True
    return False


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)
    lower_bound = int(input_text.split("-")[0])
    upper_bound = int(input_text.split("-")[1])
    passwords = {n for n in range(lower_bound, upper_bound) if check_adjacent(n) and check_increasing(n)}
    return len(passwords)


if __name__ == "__main__":
    run_main(main)
