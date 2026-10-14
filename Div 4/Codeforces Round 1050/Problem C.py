t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    
    current_time = 0
    current_side = 0
    total_points = 0
    
    for i in range(n):
        next_time, next_side = map(int, input().split())
        
        dt = next_time - current_time
        db = abs(next_side - current_side)
        
        if (dt - db) % 2 == 0:
            total_points += dt
        else:
            total_points += dt - 1
            
        current_time = next_time
        current_side = next_side
        
    total_points += m - current_time
    print(total_points)
