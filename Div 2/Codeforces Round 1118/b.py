t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    carrots = list(map(int, input().split()))
    
    count = [0] * (2 * m + 2)
    for size in carrots:
        count[size] += 1
        
    max_carrots = 0
    greater_or_equal = 0
    
    for L in range(m, 0, -1):
        greater_or_equal += count[L]
        
        total_possible = greater_or_equal + count[2 * L]
        
        if total_possible > max_carrots:
            max_carrots = total_possible
            
    print(max_carrots)
