for _ in range(int(input())):
    n = int(input())
    s = input()

    base_len = 1 
    for i in range(1, n):
        if s[i] != s[i-1]:
            base_len += 1
    min_change = 0

    for i in range(1, n - 1):
        if s[i-1] == s[i+1]:
            if s[i] != s[i-1]:
                min_change = min(min_change, -2)
        else:
            if s[i] == s[i-1] or s[i] == s[i+1]:
                pass
            else:
                min_change = min(min_change, -1)

    print(base_len + min_change)