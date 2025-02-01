from collections import deque

class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

class Graph:
    def __init__(self, root):
        self._root = root

    @property
    def root(self):
        return self._root

    def dfs(self, node, visited = None):
        if visited is None:
            visited = []
        if node in visited:
            return visited
        visited.append(node)
        for next_node in node.outbound:
            self.dfs(next_node, visited)
        return visited

    def bfs(self, vertex):
        visited = set()
        queue = deque()
        queue.append(vertex)
        visited.add(vertex)
        result = []
        while queue:
            current_vertex = queue.popleft()
            result.append(current_vertex)
            for next_vertex in current_vertex.outbound:
                if next_vertex not in visited:
                    queue.append(next_vertex)
                    visited.add(next_vertex)
        return result


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)

visited_nodes = g.dfs(g.root)
print('DFS:', *[str(node) for node in visited_nodes])

visited_nodes_2 = g.bfs(g.root)
print('BFS:', *[str(ver) for ver in visited_nodes_2])

