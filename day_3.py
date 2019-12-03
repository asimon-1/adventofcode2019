from utils import get_input, run_main
import numpy as np


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)
    (wire1, wire2) = input_text.splitlines()
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")
    
    mask1 = set()
    mask2 = set()
    coords1 = [0,0]
    coords2 = [0,0]
    for (instr1, instr2) in zip(wire1, wire2):
        dir1 = instr1[0]
        step1 = int(instr1[1:])
        dir2 = instr2[0]
        step2 = int(instr2[1:])

        for _ in range(step1):
            mask1.add(tuple(coords1))
            if dir1 == "U":
                coords1[1] += 1
            elif dir1 == "R":
                coords1[0] += 1
            elif dir1 == "D":
                coords1[1] -= 1
            elif dir1 == "L":
                coords1[0] -= 1
        for _ in range(step2):
            mask2.add(tuple(coords2))
            if dir2 == "U":
                coords2[1] += 1
            elif dir2 == "R":
                coords2[0] += 1
            elif dir2 == "D":
                coords2[1] -= 1
            elif dir2 == "L":
                coords2[0] -= 1
    intersections = mask1.intersection(mask2)
    distances = {abs(inter[0]) + abs(inter[1]) for inter in intersections if inter != (0,0)}
    print(distances)

    return min(distances)

if __name__ == "__main__":
    run_main(main)
