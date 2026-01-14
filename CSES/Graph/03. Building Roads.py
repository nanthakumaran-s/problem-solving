from collections import defaultdict

class DSU:
    def __init__(self, size):
        self.size = [1] * size
        self.parent = [None] * size
        for i in range(size):
            self.parent[i] = i
    
    def find(self, node):
        if self.parent[node] == node: return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)
        if u_parent == v_parent: return
        if self.size[u_parent] > self.size[v_parent]:
            self.parent[v_parent] = u_parent
            self.size[u_parent] += self.size[v_parent]
        else:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]

class solve():
    n, m = map(int, input().split())
    dsu = DSU(n)

    for _ in range(m):
        u, v = map(int, input().split())
        dsu.union(u - 1, v - 1)
    
    components = []
    for node in range(n):
        if dsu.find(node) == node:
            components.append(node)
    
    if components:
        print(len(components) - 1)
        for i in range(len(components) - 1):
            print(f"{components[i] + 1} {components[i + 1] + 1}")
    else:
        print(0)

solve()
