from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    vis = [False] * n
    team = ["0"] * n

    def bfs(node):
        q = deque()
        q.append(node)
        vis[node] = True
        team[node] = "1"

        while q:
            node = q.popleft()
            for adj in graph[node]:
                if not vis[adj]:
                    vis[adj] = True
                    team[adj] = "1" if team[node] == "2" else "2"
                    q.append(adj)
                else:
                    if team[node] == team[adj]:
                        return False
        return True
    
    for i in range(n):
        if not vis[i]:
            if not bfs(i):
                print("IMPOSSIBLE")
                return
    
    print(" ".join(team))

solve()