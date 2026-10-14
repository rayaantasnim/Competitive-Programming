t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    best_score = 0
    best_i = -1
    best_j = -1
    
    last_one = -1
    first_cand = -1
    any_cand = -1

    for j in range(n):
        if a[j] != 0:
            if any_cand == -1:
                any_cand = j
            if first_cand == -1:
                first_cand = j

            if last_one != -1:
                score = j - last_one + 1
                if score > best_score:
                    best_score = score
                    best_i = last_one
                    best_j = j
            elif first_cand != -1 and first_cand < j:
                score = j - first_cand + 1
                if score > best_score:
                    best_score = score
                    best_i = first_cand
                    best_j = j

            if a[j] == 1:
                last_one = j

    ans = [0 if x == -1 else x for x in a]

    if best_score > 0:
        ans[best_i] = 1
        ans[best_j] = 1
    elif any_cand != -1:
        ans[any_cand] = 1

    print(*(ans))
