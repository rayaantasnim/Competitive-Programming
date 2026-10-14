for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    current_max = 0
    for x in a:
        current_max = max(current_max, x)
        ans += current_max

    for i in range(n):
        for j in range(i + 1, n):
            a[i], a[j] = a[j], a[i]

            new_total = 0
            temp_max = 0
            for x in a:
                temp_max = max(temp_max, x)
                new_total += temp_max

            ans = max(ans, new_total)
            a[i], a[j] = a[j], a[i]

    print(ans)
