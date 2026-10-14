t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    a = []
    b = []
    
    for i in range(n):
        if p[i] != i + 1:
            a.append(p[i])
            b.append(i + 1)
            
    if len(a) == 0:
        print("YES")
    else:
        a.reverse()
        if a == b:
            print("YES")
        else:
            print("NO")
