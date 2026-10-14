t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    odds = 0
    mod0 = 0
    mod2 = 0
    
    for x in a:
        if x % 2 != 0:
            odds += 1
        elif x % 4 == 0:
            mod0 += 1
        else:
            mod2 += 1
            
    ans = max(odds, mod0, mod2)
    print(ans)
