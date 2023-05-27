import random
from operator import sub

from enums.CellType import CellType


class Pattern:
    difficulty: int         # gives the width and height of pattern (if one subtracted, due to 0-indexation)
    start: (int, int)       # starting cell: initial bunny position
    end: (int, int)         # final cell: carrot position
    displacement = [(-1, -1), (-1, 1), (1, 1), (1, -1)]     # displacement which can be caused by a jump action
    weights: list[int]                                      # weights[i] = chance of picking displacement[i]
    initial_pattern: list[list[CellType]]   # pattern as it is initially generated (bunny on start)
    current_pattern: list[list[CellType]]   # pattern in xth moment of game (bunny at bunny_position)
    bunny_position: (int, int)              # current bunny position, initially start
    optimal_path: list[(int, int)]          # the shortest path from start to end, respecting traps

    def __init__(self):
        pass

    # called each time difficulty changes
    def reset(self, difficulty):
        print("enter reset")
        self.difficulty = difficulty

        # generate a random start, end and weights
        d = difficulty - 1
        self.start, self.end, self.weights = random.choice([
            [(0, 0), (d, d), [1, 3, 5, 3]],   # up left    -> down right
            [(0, d), (d, 0), [3, 1, 3, 5]],   # up right   -> down left
            [(d, d), (0, 0), [5, 3, 1, 3]],   # down right -> up left
            [(d, 0), (0, d), [3, 5, 3, 1]]])  # down left  -> up right

        empty_path = self.generate_random_path(self.start, self.end)                # path on which no traps will spawn
        print(f"empty path: {empty_path}")
        self.initial_pattern = self.current_pattern = self.make_pattern(empty_path)  # pattern generated w.r.t. path
        print("initial pattern:")
        self.print_current_pattern()
        self.optimal_path = self.get_optimal_path(self.initial_pattern)              # A* algorithm on the pattern
        print(f"optimal path: {self.optimal_path}")

        self.bunny_position = self.start  # this is modified outside of class, but needs to be initialized

    def print_current_pattern(self):
        for row in self.current_pattern:
            print(*row, sep=' ')

    # generates a path from start till end, so it will be left clear => patterns always solvable
    def generate_random_path(self, start, end):
        stack = [start]
        visited = set()

        while stack:
            vertex = stack.pop()
            if vertex == end:
                return visited  # destination found, (unordered) set of cells belonging to path can be returned

            if vertex in visited:
                continue  # invalid since visited (avoid looping around), backtrack (popped and discarded)

            i, j = vertex
            if i < 0 or j < 0 or i > self.difficulty - 1 or j > self.difficulty - 1:
                continue  # invalid since out of bounds, backtrack

            visited.add(vertex)  # valid, mark as visited (path of path)

            # https://softwareengineering.stackexchange.com/questions/233541/how-to-implement-a-weighted-shuffle
            order = sorted(range(len(self.displacement)), key=lambda k: random.random() ** (1.0 / self.weights[k]))

            # options processed in the order the weighted shuffle gave us
            for index in order:
                stack.append(tuple(map(sub, (i, j), self.displacement[index])))

        print("Failed path generation")
        return None

    def make_pattern(self, empty_path):
        # the pattern to be returned, originally filled with empty cells
        pattern = [[CellType.Empty for _ in range(self.difficulty)] for _ in range(self.difficulty)]

        dont_care_cells = [CellType.Trap, CellType.Empty]  # cell types which can be used for filling unreachable cells
        dont_care_weights = [5, 7]                         # and the associated weights

        si, sj = self.start
        bunny_cell_parity = (si + sj) % 2
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                if (i + j) % 2 != bunny_cell_parity:  # due to diagonal jumps, such cells are unreachable
                    pattern[i][j] = random.choices(dont_care_cells, weights=dont_care_weights, k=1)[0]
                elif (i, j) not in empty_path:
                    pattern[i][j] = CellType.Trap

        bi, bj = self.start
        ci, cj = self.end
        pattern[bi][bj] = CellType.Bunny
        pattern[ci][cj] = CellType.Carrot

        return pattern

    # node class used for A* algorithm, to think about the problem with graphs
    class Node:
        def __init__(self, parent, position):
            self.parent = parent
            self.position = position
            self.g = 0  # cost of moving from initial cell to current cell
            self.h = 0  # heuristic (estimate) cost of reaching final cell from current cell
            self.f = 0  # final cost function = g + h

        def __eq__(self, other):
            return self.position == other.position

    # https://www.educative.io/answers/what-is-the-a-star-algorithm
    def get_optimal_path(self, pattern):
        si, sj = self.start
        ei, ej = self.end
        current_node = Pattern.Node(None, (si, sj))
        goal_node = Pattern.Node(None, (ei, ej))
        goal_node.g = goal_node.h = goal_node.f = 0

        open_list = []      # nodes available for processing in a step
        closed_list = []    # nodes already processed
        open_list.append(current_node)

        while len(open_list) > 0:
            # search for node with smallest f (and its index)
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # move current to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # if goal found, path can be reconstructed by backtracking to start and taking the inverse of resulting list
            if current_node == goal_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]

            # iterate through neighboring cells
            children = []  # list of valid children (neighbors)
            for new_position in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
                node_position = (current_node.position[0] + new_position[0],
                                 current_node.position[1] + new_position[1])

                if node_position[0] >= self.difficulty \
                        or node_position[0] < 0 \
                        or node_position[1] >= self.difficulty \
                        or node_position[1] < 0:
                    continue  # discard if out of bounds

                if pattern[node_position[0]][node_position[1]] == CellType.Trap:
                    continue  # discard if trap

                new_node = Pattern.Node(current_node, node_position)
                children.append(new_node)

            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # cost of getting to child = cost to get here + 1
                child.g = current_node.g + 1

                # perfect heuristics for this problem: Euclidean distance
                child.h = ((child.position[0] - goal_node.position[0]) ** 2) + \
                          ((child.position[1] - goal_node.position[1]) ** 2)

                # as always, total cost = cost till now + heuristics
                child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                open_list.append(child)

        return None
