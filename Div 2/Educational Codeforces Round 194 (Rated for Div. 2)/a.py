import collections

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    zeros = a.count(0)
    
    if zeros < 2:
        if n == 2 and zeros == 2:
            print(0)
        else:
            print(-1)
    else:
        ans = 0
        if a[0] == 1:
            ans += 1
        if a[-1] == 1:
            ans += 1
        print(ans)
