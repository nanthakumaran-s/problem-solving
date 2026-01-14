from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    
    vis = [[False] * m for _ in range(n)]

    def dfs(i, j):
        vis[i][j] = True
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == "." and not vis[ni][nj]:
                dfs(ni, nj)
    
    def bfs(i, j):
        q = deque()
        q.append((i,j))
        while q:
            i, j = q.popleft()
            if vis[i][j]: continue
            vis[i][j] = True
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == "." and not vis[ni][nj]:
                    q.append((ni, nj))
    
    COUNT = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "." and not vis[i][j]:
                COUNT += 1
                bfs(i, j)
    print(COUNT)
    

solve()