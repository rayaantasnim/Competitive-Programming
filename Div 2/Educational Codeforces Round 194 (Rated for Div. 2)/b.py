for i in range(int(input())):
    x, y, k = map(int, input().split())
    
    d = y - x
    total = 0
    i = 0
    
    while i < k and x + i <= d:
        total += d % (x + i)
        i += 1
        
    if i < k:
        total += (k - i) * d
        
    print(total)
