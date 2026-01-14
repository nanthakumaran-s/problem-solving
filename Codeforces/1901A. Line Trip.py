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
    n, x = get_ints()
    arr = list(get_ints())

    MAX = arr[0]

    for i in range(1, n):
        MAX = max(MAX, (arr[i] - arr[i - 1]))
    
    MAX = max(MAX, (x - arr[-1]) * 2)
    write(MAX)


"""
Initial Handling
"""
if __name__ == "__main__":
    t = get_int()
    # t = 1
    for _ in range(t):
        solve()
    sys.stdout.write("\n".join(out))