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
    n = get_int()
    arr = list(get_ints())

    tree = defaultdict(list)
    for i in range(len(arr)):
        tree[arr[i]].append(i + 2)

    subord = [0] * n
    st = [(1, 0)]

    while st:
        node, state = st.pop()

        if state == 0:
            st.append((node, 1))
            for child in tree[node]:
                st.append((child, 0))
            
        if state == 1:
            res = len(tree[node])
            for child in tree[node]:
                res += subord[child - 1]
            subord[node - 1] = res
    
    write(subord)
    return

    
    def rec(node):
        if len(tree[node]) == 0:
            return 1
        res = 0
        for child in tree[node]:
            res += rec(child)
        subord[node - 1] = res
        return res + 1
    
    rec(1)
    write(subord)

"""
Initial Handling
"""
if __name__ == "__main__":
    # t = get_int()
    t = 1
    for _ in range(t):
        solve()
    sys.stdout.write("\n".join(out))