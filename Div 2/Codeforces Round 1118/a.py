import math
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = math.gcd(a[0], a[-1])
    print(ans)
