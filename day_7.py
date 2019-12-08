from utils import get_input, run_main
from itertools import permutations


class Computer:
    def __init__(self, intcode):
        self.intcode = intcode.copy()
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

    def run_opcode(self, inp1, inp2):
        while self.run:
            opcode = self.intcode[self.pointer]
            operation = opcode % 100
            mode1 = opcode // 10 ** 2 % 10
            mode2 = opcode // 10 ** 3 % 10
            mode3 = opcode // 10 ** 4 % 10
            kwargs = {"mode1": mode1, "mode2": mode2, "mode3": mode3, "inp": inp1 if not self.pointer else inp2}
            self.mapping[operation](**kwargs)

        return self.out


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)
    original_intcode = [int(x) for x in input_text.split(",")]

    computerA = Computer(original_intcode)
    computerB = Computer(original_intcode)
    computerC = Computer(original_intcode)
    computerD = Computer(original_intcode)
    computerE = Computer(original_intcode)

    max_val = 0
    signal = None
    all_phase_settings = permutations(list(range(5)))
    for phase_settings in all_phase_settings:

        computerA = Computer(original_intcode)
        computerB = Computer(original_intcode)
        computerC = Computer(original_intcode)
        computerD = Computer(original_intcode)
        computerE = Computer(original_intcode)

        val = computerE.run_opcode(
            phase_settings[4],
            computerD.run_opcode(
                phase_settings[3],
                computerC.run_opcode(
                    phase_settings[2],
                    computerB.run_opcode(phase_settings[1], computerA.run_opcode(phase_settings[0], 0,),),
                ),
            ),
        )

        max_val = val if val > max_val else max_val
        signal = phase_settings if val > max_val else signal

    return max_val


if __name__ == "__main__":
    run_main(main)
