t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    s = input()
    
    ans = 0
    
    for i in range(0, n, k):
        farm = s[i : i + k]
        if '0' not in farm:
            ans += 1
            
    print(ans)
