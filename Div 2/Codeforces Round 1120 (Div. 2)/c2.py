def solve():
    MOD = 1000000007
    
    try:
        t_cases = int(input())
    except (EOFError, ValueError):
        return

    for _ in range(t_cases):
        try:
            n = int(input())
            a = [0] + [int(x) for x in input().split()]
        except (EOFError, ValueError):
            break
            
        forbidden = [False] * n
        for k in range(1, n + 1):
            val = a[k]
            L = val * k
            R = (val + 1) * k - 1
            start = max(0, L)
            end = min(n - 1, R)
            if start <= end:
                for i in range(start, end + 1):
                    forbidden[i] = True
                    
        intervals = []
        possible = True
        for k in range(1, n + 1):
            val = a[k]
            for target in range(val):
                L = target * k
                R = (target + 1) * k - 1
                if L >= n:
                    possible = False
                    break
                R = min(n - 1, R)
                intervals.append((L, R))
            if not possible:
                break
                
        if not possible:
            print(0)
            continue
            
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        valid_intervals = []
        for L, R in intervals:
            cleaned_L, cleaned_R = -1, -1
            for i in range(L, R + 1):
                if not forbidden[i]:
                    if cleaned_L == -1:
                        cleaned_L = i
                    cleaned_R = i
            if cleaned_L == -1:
                possible = False
                break
            valid_intervals.append((cleaned_L, cleaned_R))
            
        if not possible:
            print(0)
            continue
            
        valid_intervals.sort(key=lambda x: x[1])
        
        active_points = []
        for i in range(n):
            if not forbidden[i]:
                active_points.append(i)
                
        ans = 1
        pt_idx = 0
        m = len(active_points)
        
        taken = [False] * m
        available_choices = 0
        
        interval_idx = 0
        num_intervals = len(valid_intervals)
        
        for i in range(m):
            curr_pt = active_points[i]
            
            while interval_idx < num_intervals and valid_intervals[interval_idx][1] < curr_pt:
                interval_idx += 1
                
            choices_for_this = 1
            if not taken[i]:
                choices_for_this += 1
                
            ans = (ans * choices_for_this) % MOD
            
        print(ans)

if __name__ == '__main__':
    solve()
