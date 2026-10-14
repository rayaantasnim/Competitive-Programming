t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    total_counts = [0] * (n + 1)
    for x in a:
        total_counts[x] += 1

    possible = True
    target = [0] * (n + 1)
    for x in range(1, n + 1):
        if total_counts[x] > 0:
            if total_counts[x] % k != 0:
                possible = False
                break
            target[x] = total_counts[x] // k

    if not possible:
        print(0)
        continue

    ans = 0
    current_counts = [0] * (n + 1)
    l = 0

    for r in range(n):
        right_num = a[r]
        current_counts[right_num] += 1

        while current_counts[right_num] > target[right_num]:
            left_num = a[l]
            current_counts[left_num] -= 1
            l += 1

        ans += (r - l + 1)

    print(ans)
