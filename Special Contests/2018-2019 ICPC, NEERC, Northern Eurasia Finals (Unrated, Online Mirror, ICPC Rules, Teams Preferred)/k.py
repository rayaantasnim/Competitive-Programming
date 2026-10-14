import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    q = int(data[0])
    MAX_T = 1000005 
    
    tree_sum = [0] * (2 * MAX_T)
    tree_max = [0] * (2 * MAX_T)
    
    for i in range(MAX_T):
        tree_max[MAX_T + i] = i

    def update(pos, d, is_add):
        idx = MAX_T + pos
        if is_add:
            tree_sum[idx] = d
            tree_max[idx] = pos + d
        else:
            tree_sum[idx] = 0
            tree_max[idx] = pos
            
        idx //= 2
        while idx > 0:
            left = 2 * idx
            right = 2 * idx + 1
            tree_sum[idx] = tree_sum[left] + tree_sum[right]
            tree_max[idx] = max(tree_max[left] + tree_sum[right], tree_max[right])
            idx //= 2

    def query(r):
        l_idx = MAX_T + 1
        r_idx = MAX_T + r + 1 
        
        left_sums = []
        left_maxs = []
        right_sums = []
        right_maxs = []
        
        while l_idx < r_idx:
            if l_idx % 2 == 1:
                left_sums.append(tree_sum[l_idx])
                left_maxs.append(tree_max[l_idx])
                l_idx += 1
            if r_idx % 2 == 1:
                r_idx -= 1
                right_sums.append(tree_sum[r_idx])
                right_maxs.append(tree_max[r_idx])
            l_idx //= 2
            r_idx //= 2
            
        right_sums.reverse()
        right_maxs.reverse()
        
        all_sums = left_sums + right_sums
        all_maxs = left_maxs + right_maxs
        
        if not all_maxs:
            return 0
            
        current_sum = all_sums[0]
        current_max = all_maxs[0]
        
        for i in range(1, len(all_maxs)):
            current_max = max(current_max + all_sums[i], all_maxs[i])
            current_sum += all_sums[i]
            
        return current_max

    events = [None] * (q + 1)
    output = []
    
    ptr = 1
    event_idx = 1
    while event_idx <= q:
        type_str = data[ptr]
        if type_str == '+':
            t = int(data[ptr+1])
            d = int(data[ptr+2])
            events[event_idx] = (t, d)
            update(t, d, True)
            ptr += 3
        elif type_str == '-':
            i = int(data[ptr+1])
            t, d = events[i]
            update(t, d, False)
            ptr += 2
        elif type_str == '?':
            t = int(data[ptr+1])
            max_end_time = query(t)
            wait_time = max_end_time - t
            if wait_time < 0:
                wait_time = 0
            output.append(str(wait_time))
            ptr += 2
        event_idx += 1
        
    print('\n'.join(output))

if __name__ == '__main__':
    solve()
