"""
Imports
"""
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop
import sys

"""
Template
"""
input = sys.stdin.readline

get_int = lambda: int(input())
get_ints = lambda: map(int, input().split())
get_str = lambda: input().strip()
get_strs = lambda: input().split()

out = []
write = lambda x: out.append(
    " ".join(map(str, x)) if isinstance(x, (list, tuple)) else str(x)
)

"""
Code here
"""
def solve():
    n = get_int()
    s = get_str()

    free_count = 0
    ans = 0

    for i in range(n):
        if s[i] == "#" and free_count != 0:
            if free_count >= 3:
                write(2)
                return
            ans += 1 if free_count == 1 else 2
            free_count = 0
        if s[i] == ".":
            free_count += 1
    
    if free_count >= 3:
        write(2)
        return
    elif free_count:
        ans += 1 if free_count == 1 else 2
    
    write(ans)

"""
Initial Handling
"""
if __name__ == "__main__":
    t = get_int()
    # t = 1
    for _ in range(t):
        solve()
    sys.stdout.write("\n".join(out))