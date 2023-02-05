
class Node:

    def __init__(self, position, parent, total_cost: int, step_cost: int):
        self.position = position
        self.parent = parent
        self.total_cost = total_cost
        self.step_cost = step_cost

    def __str__(self):
        return ("({}, {})".format(self.position[0], self.position[1]))