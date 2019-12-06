from utils import get_input, run_main


class Obj:
    def __init__(self, parent_name=None):
        self.parent = None
        self.parent_name = parent_name

    def update_parent(self, container):
        if self.parent_name is not None:
            self.parent = container[self.parent_name]

    def count_orbits(self):
        try:
            return self.parent.count_orbits() + 1
        except AttributeError:
            return 0


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)

    if not part_2:
        # Instantiate all objects
        container = {line.split(")")[1]: Obj(line.split(")")[0]) for line in input_text.splitlines()}
        container.update({"COM": Obj(None)})

        # Link all objects
        [obj.update_parent(container) for obj in container.values()]

        # Count Orbits
        return sum([o.count_orbits() for o in container.values()])


if __name__ == "__main__":
    run_main(main)
