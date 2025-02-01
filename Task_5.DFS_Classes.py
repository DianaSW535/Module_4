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

    def dfs(self, node, visited = None):
        if visited is None:
            visited = []
        if node in visited:
            return visited
        visited.append(node)
        for next_node in node.outbound:
            self.dfs(next_node, visited)
        return visited

    @property
    def root(self):
        return self._root


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
print(*[str(node) for node in visited_nodes])
