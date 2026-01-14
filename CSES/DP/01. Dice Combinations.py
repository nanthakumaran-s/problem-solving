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
    num = get_int()

    dp = [0] * (num + 1)
    dp[0] = 1

    for n in range(1, num + 1):
        for i in range(1, 7):
            if n - i >= 0:
                dp[n] = (dp[n] + dp[n - i]) % MOD
    
    write(dp[num])
    return

    @lru_cache(None)
    def dp(n):
        if n == 0:
            return 1
        
        res = 0
        for i in range(1, 7):
            if n - i >= 0:
                res = (res + dp(n - i)) % MOD
        return res

    write(dp(num))

"""
Initial Handling
"""
if __name__ == "__main__":
    # t = get_int()
    t = 1
    for _ in range(t):
        solve()
    sys.stdout.write("\n".join(out))