from dataclasses import dataclass

from utils import get_input


@dataclass
class Point:
    x: int
    y: int

@dataclass
class Node:
    height: int
    previous: Point = None
    visited: bool = False
    cost: int = None

@dataclass
class Graph:
    nodes: list[list[Node]]
    start: Node = None
    end: Node = None

    def possible_directions(self, start_point: Point):
            x_exists = lambda x: 0 <= x < len(self.nodes[0])
            y_exists = lambda y: 0 <= y < len(self.nodes)

            possible_directions = [
                Point(x, y) for x, y in [
                    (start_point.x, start_point.y - 1),
                    (start_point.x, start_point.y + 1),
                    (start_point.x - 1, start_point.y),
                    (start_point.x + 1, start_point.y),
                ] if x_exists(x) and y_exists(y)
            ]
            max_height = self.nodes[start_point.y][start_point.x].height + 1

            return [point for point in possible_directions if self.get_node(point).height <= max_height]

    def get_node(self, point: Point) -> Node:
        return self.nodes[point.y][point.x]

    def traverse(self, queue = None) -> None:
        if not queue:
            queue = [(0, self.start, self.start)]
        while queue:
            curr_cost, curr_point, prev_point = queue.pop(0)
            if not self.get_node(curr_point).visited:
                self.get_node(curr_point).cost = curr_cost
                self.get_node(curr_point).visited = True
                self.get_node(curr_point).previous = prev_point
                if curr_point == self.end:
                    break
                else:
                    curr_cost += 1
                    for next_point in self.possible_directions(curr_point):
                        queue.append((curr_cost, next_point, curr_point))
                    queue = sorted(queue, key=lambda l: l[0])

def load_graph(data) -> Graph:
    graph = Graph([])
    for row in data:
        graph.nodes.append([])
        for point in row:
            if point == "S":
                graph.start = Point(
                    x=len(graph.nodes[-1]),
                    y=len(graph.nodes) - 1
                )
                point = "a"
            elif point == "E":
                graph.end = Point(
                    x=len(graph.nodes[-1]),
                    y=len(graph.nodes) - 1
                )
                point = "z"
            graph.nodes[-1].append(Node(height=ord(point) - ord("a")))
    return graph

def part_one(data):
    graph = load_graph(data)
    graph.traverse()
    return graph.get_node(graph.end).cost

def part_two(data):
    graph = load_graph(data)
    queue = []
    for y in range(len(graph.nodes)):
        for x in range(len(graph.nodes[0])):
            point = Point(x, y)
            if graph.get_node(point).height == 0:
                queue.append((0, point, point))
    graph.traverse(queue=queue)
    return graph.get_node(graph.end).cost

if __name__ == "__main__":
    path = 'data/12.txt'
    data = get_input(path)

    print(part_one(data))
    print(part_two(data))
