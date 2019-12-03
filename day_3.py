from utils import get_input, run_main
from dataclasses import dataclass, field


@dataclass
class Wire:
    instructions: tuple
    dir_map: dict = field(default_factory=lambda: {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)})
    current_instruction: int = 0
    path: list = field(default_factory=lambda: [(0, 0)])

    def execute_next_instruction(self):
        direction = self.instructions[self.current_instruction][0]
        additional_steps = self.instructions[self.current_instruction][1]
        last_position = self.path[-1]

        additional_path = [
            (
                last_position[0] + (_ + 1) * self.dir_map[direction][0],
                last_position[1] + (_ + 1) * self.dir_map[direction][1],
            )
            for _ in range(additional_steps)
        ]
        self.path += additional_path
        self.current_instruction += 1

    def execute_all_instructions(self):
        while self.current_instruction < len(self.instructions):
            self.execute_next_instruction()


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)
    (wire1, wire2) = input_text.splitlines()
    wire1_instructions = tuple((instr[0], int(instr[1:])) for instr in wire1.split(","))
    wire2_instructions = tuple((instr[0], int(instr[1:])) for instr in wire2.split(","))

    wire1 = Wire(wire1_instructions)
    wire2 = Wire(wire2_instructions)

    wire1.execute_all_instructions()
    wire2.execute_all_instructions()

    intersections = set(wire1.path).intersection(set(wire2.path))

    if not part_2:
        # Manhattan Distance
        distances = {abs(inter[0]) + abs(inter[1]) for inter in intersections if inter != (0, 0)}

    else:
        # Minimum steps
        distances = {wire1.path.index(inter) + wire2.path.index(inter) for inter in intersections if inter != (0, 0)}

    return min(distances)


if __name__ == "__main__":
    run_main(main)
