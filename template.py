"""
Imports
"""
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop
from functools import lru_cache
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

MOD = 10**9 + 7

"""
Code here
"""
def solve():
    pass

"""
Initial Handling
"""
if __name__ == "__main__":
    t = get_int()
    # t = 1
    for _ in range(t):
        solve()
    sys.stdout.write("\n".join(out))