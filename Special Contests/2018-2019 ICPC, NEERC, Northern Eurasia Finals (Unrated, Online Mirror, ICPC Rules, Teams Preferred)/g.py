import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    ptr = 1
    
    output = []
    for _ in range(t):
        k = int(data[ptr])
        a = [int(x) for x in data[ptr+1:ptr+8]]
        ptr += 8
        
        weeks_class = sum(a)
        
        full_weeks = (k - 1) // weeks_class
        rem_k = k - (full_weeks * weeks_class)
        mid_days = full_weeks * 7
        
        min_extra_days = 10**18
        
        for start_day in range(7):
            counted_class = 0
            days_passed = 0
            current_day = start_day
            
            while counted_class < rem_k:
                if a[current_day] == 1:
                    counted_class += 1
                days_passed += 1
                current_day = (current_day + 1) % 7
                
            if days_passed < min_extra_days:
                min_extra_days = days_passed
                
        output.append(str(mid_days + min_extra_days))
        
    print('\n'.join(output))

if __name__ == '__main__':
    solve()
