from collections import deque

def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    
    vis = [[False] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]

    start, end = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "A":
                start = (i, j)
            if grid[i][j] == "B":
                end = (i, j)
    
    q = deque()
    q.append(start)
    vis[start[0]][start[1]] = True

    flag = False
    while q:
        (i, j) = q.popleft()
        if (i,j) == end:
            flag = True
            break
        for dx, dy, dp in [(0,1,'R'), (0,-1,'L'), (1,0,'D'), (-1,0,'U')]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != "#" and not vis[ni][nj]:
                vis[ni][nj] = True
                parent[ni][nj] = dp
                q.append((ni, nj))

    if not flag:
        print("NO")
        return

    path = []
    i, j = end[0], end[1]
    while (i, j) != start:
        path.append(parent[i][j])
        if parent[i][j] == "U":
            i += 1
        elif parent[i][j] == "D":
            i -= 1
        elif parent[i][j] == "L":
            j += 1
        elif parent[i][j] == "R":
            j -= 1
        else:
            break
    print("YES")
    print(len(path))
    path = path[::-1]
    print("".join(path))

solve()
