from utils import get_input, run_main
from itertools import product


class Computer:
    def __init__(self, intcode):
        self.original_intcode = intcode
        self.intcode = intcode
        self.pointer = 0
        self.run = 1
        self.out = 0
        self.mapping = {
            1: self.addition,
            2: self.multiplication,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equal,
            99: self.exit,
        }

    def addition(self, mode1, mode2, mode3, **kwargs):
        param1 = self.intcode[self.pointer + 1]
        param2 = self.intcode[self.pointer + 2]
        param3 = self.intcode[self.pointer + 3]
        val1 = param1 if mode1 else self.intcode[param1]
        val2 = param2 if mode2 else self.intcode[param2]

        if mode3:
            # Immediate
            raise RuntimeError
        else:
            # Position
            self.intcode[param3] = val1 + val2
        self.pointer += 4


    def multiplication(self, mode1, mode2, mode3, **kwargs):
        param1 = self.intcode[self.pointer + 1]
        param2 = self.intcode[self.pointer + 2]
        param3 = self.intcode[self.pointer + 3]
        val1 = param1 if mode1 else self.intcode[param1]
        val2 = param2 if mode2 else self.intcode[param2]
        if mode3:
            # Immediate
            raise RuntimeError
        else:
            # Position
            self.intcode[param3] = val1 * val2
        self.pointer += 4


    def input(self, inp, **kwargs):
        param1 = self.intcode[self.pointer + 1]
        self.intcode[param1] = inp
        self.pointer += 2


    def output(self, mode1, **kwargs):
        param1 = self.intcode[self.pointer + 1]
        self.pointer += 2
        self.out = param1 if mode1 else self.intcode[param1]


    def jump_if_true(self, mode1, mode2, **kwargs):
        param1 = self.intcode[self.pointer + 1]
        param2 = self.intcode[self.pointer + 2]
        val1 = param1 if mode1 else self.intcode[param1]
        val2 = param2 if mode2 else self.intcode[param2]
        self.pointer = val2 if val1 else self.pointer + 3


    def jump_if_false(self, mode1, mode2, **kwargs):
        param1 = self.intcode[self.pointer + 1]
        param2 = self.intcode[self.pointer + 2]
        val1 = param1 if mode1 else self.intcode[param1]
        val2 = param2 if mode2 else self.intcode[param2]
        self.pointer = val2 if not val1 else self.pointer + 3


    def less_than(self, mode1, mode2, **kwargs):
        param1 = self.intcode[self.pointer + 1]
        param2 = self.intcode[self.pointer + 2]
        param3 = self.intcode[self.pointer + 3]
        val1 = param1 if mode1 else self.intcode[param1]
        val2 = param2 if mode2 else self.intcode[param2]
        if val1 < val2:
            self.intcode[param3] = 1
        else:
            self.intcode[param3] = 0
        self.pointer += 4


    def equal(self, mode1, mode2, **kwargs):
        param1 = self.intcode[self.pointer + 1]
        param2 = self.intcode[self.pointer + 2]
        param3 = self.intcode[self.pointer + 3]
        val1 = param1 if mode1 else self.intcode[param1]
        val2 = param2 if mode2 else self.intcode[param2]
        if val1 == val2:
            self.intcode[param3] = 1
        else:
            self.intcode[param3] = 0
        self.pointer += 4

    def exit(self, **kwargs):
        self.run = 0

    def run_opcode(self, inp):
        out = 0

        # Run the intcode
        while self.run:
            opcode = self.intcode[self.pointer]
            operation = opcode % 100
            mode1 = opcode // 10 ** 2 % 10
            mode2 = opcode // 10 ** 3 % 10
            mode3 = opcode // 10 ** 4 % 10
            kwargs = {"mode1":mode1, "mode2":mode2, "mode3":mode3, "inp":inp}
            self.mapping[operation](**kwargs)

        return self.out


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)
    if test:
        if not part_2:
            original_intcode = [int(x) for x in input_text.splitlines()[0].split(",")]
        else:
            original_intcode = [int(x) for x in input_text.splitlines()[1].split(",")]
    else:
        original_intcode = [int(x) for x in input_text.split(",")]

    if not part_2:
        inp = 1
    else:
        if test:
            inp = 8
        else:
            inp = 5

    computer = Computer(original_intcode)

    return computer.run_opcode(inp)


if __name__ == "__main__":
    run_main(main)
