t = int(input())

for _ in range(t):
    n = int(input())
    arrays = []
    max_len = 0
    
    for _ in range(n):
        row = list(map(int, input().split()))
        k = row[0]
        elements = row[1:]
        arrays.append(elements)
        if k > max_len:
            max_len = k
            
    by_len = [[] for _ in range(max_len + 1)]
    for idx, arr in enumerate(arrays):
        by_len[len(arr)].append(idx)
        
    array_rank = [0] * n
    dp_rank = [0] * (max_len + 2)
    best_array_at_l = [0] * max_len
    active_arrays = []
    
    for l in range(max_len - 1, -1, -1):
        for idx in by_len[l + 1]:
            active_arrays.append(idx)
            array_rank[idx] = dp_rank[l + 1]
            
        pairs = []
        for idx in active_arrays:
            pairs.append(((arrays[idx][l], array_rank[idx]), idx))
            
        pairs.sort(key=lambda item: item[0])
        
        best_array_at_l[l] = pairs[0][1]
        
        current_rank = 0
        array_rank[pairs[0][1]] = current_rank
        
        for i in range(1, len(pairs)):
            if pairs[i][0] != pairs[i-1][0]:
                current_rank += 1
            array_rank[pairs[i][1]] = current_rank
            
        dp_rank[l] = array_rank[best_array_at_l[l]]
        
    result = []
    curr_l = 0
    while curr_l < max_len:
        best_idx = best_array_at_l[curr_l]
        arr_len = len(arrays[best_idx])
        result.extend(arrays[best_idx][curr_l:arr_len])
        curr_l = arr_len
        
    print(*(result))
