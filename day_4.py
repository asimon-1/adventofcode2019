from utils import get_input, run_main
from math import log10


def check_increasing(n):
    num_digits = int(log10(n)) + 1
    n_list = [n // 10 ** e % 10 for e in range(num_digits - 1, -1, -1)]
    return all((n_list[i + 1] - n_list[i] >= 0 for i in range(len(n_list) - 1)))


def check_adjacent(n, part_two=False):
    num_digits = int(log10(n)) + 1
    n_list = [n // 10 ** e % 10 for e in range(num_digits - 1, -1, -1)]
    digit_dict = {d: 0 for d in range(10)}
    for digit in digit_dict:
        while digit in n_list:
            n_list.remove(digit)
            digit_dict[digit] += 1
    if not part_two:
        return any({d > 1 for d in digit_dict.values()})
    else:
        return 2 in digit_dict.values()


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)
    lower_bound = int(input_text.split("-")[0])
    upper_bound = int(input_text.split("-")[1])
    passwords = {n for n in range(lower_bound, upper_bound) if check_adjacent(n, part_2) and check_increasing(n)}
    return len(passwords)


if __name__ == "__main__":
    run_main(main)
