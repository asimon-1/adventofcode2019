from utils import get_input, run_main


def main(directory, test=False, part_2=False):
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
    run_main(main)
