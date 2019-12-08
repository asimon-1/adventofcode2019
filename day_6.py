from utils import get_input, run_main


class Obj:
    def __init__(self, parent_name=None):
        self.parent = None
        self.parent_name = parent_name
        self.parents = []

    def update_parent(self, container):
        if self.parent_name is not None:
            self.parent = container[self.parent_name]

    def count_orbits(self):
        try:
            return self.parent.count_orbits() + 1
        except AttributeError:
            return 0

    def record_parents(self):
        obj = self
        while obj.parent:
            self.parents.append(obj.parent)
            obj = obj.parent


def main(directory, test=False, part_2=False):
    input_text = get_input(directory)

    # Instantiate all objects
    container = {line.split(")")[1]: Obj(line.split(")")[0]) for line in input_text.splitlines()}
    container.update({"COM": Obj(None)})

    # Link all objects
    [obj.update_parent(container) for obj in container.values()]

    if not part_2:
        # Count Orbits
        if test:
            return sum([o.count_orbits() for k,o in container.items() if k not in ("YOU", "SAN")])
        else:
            return sum([o.count_orbits() for o in container.values()])

    else:
        [obj.record_parents() for obj in container.values()]
        return len(set(container["SAN"].parents) ^ set(container["YOU"].parents))


if __name__ == "__main__":
    run_main(main)
