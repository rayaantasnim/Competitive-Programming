t = int(input())

for i in range(t):
    array = list(map(int, input().split()))

    total = sum(array)
    max_val = max(array)

    ans = -total + 2 * max_val
    print(ans)