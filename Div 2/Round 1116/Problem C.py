t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(input().strip())
    m = 2 * n
    a = [1 if c == '1' else 0 for c in s]
    if sum(a) == m:
        red = sum(1 for i in range(m) if i % 2 == 0)
        print(red, m - red)
        continue
    for _ in range(k):
        b = a[:]
        for i in range(m):
            if a[i] == 1:
                nxt = (i + 1) % m
                if a[nxt] == 0 and b[nxt] == 0 and b[i] == 1:
                    b[nxt] = 1
                    b[i] = 0
        a = b
    red = 0
    blue = 0
    for i in range(m):
        if a[i] == 1:
            if i % 2 == 0:
                red += 1
            else:
                blue += 1
    print(red, blue)