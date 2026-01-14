
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k > 1:
        print("YES")
    else:
        already_sorted = True
        for i in range(1, n):
            if a[i] < a[i - 1]:
                already_sorted = False
        if not already_sorted:
            print("NO")
        else:
            print("YES")

t = int(input())
for _ in range(t):
    solve()