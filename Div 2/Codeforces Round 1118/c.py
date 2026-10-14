import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    freq = [0] * (m + 1)
    for x in a:
        freq[x] += 1
    
    pref = [0] * (m + 1)
    for i in range(1, m + 1):
        pref[i] = pref[i - 1] + freq[i]
    
    maxfull = 0
    for L in range(1, m + 1):
        cur = 0
        j = 1
        while j * L <= m:
            left = j * L
            right = min(m, (j + 1) * L - 1)
            cur += j * (pref[right] - pref[left - 1])
            j += 1
        if cur > maxfull:
            maxfull = cur
    
    ans = [0] * (m + 1)
    LIM = 20
    
    for kk in range(1, min(m, LIM) + 1):
        P = 1 << kk
        maxcur = 0
        for L in range(1, m + 1):
            cur = 0
            j = 1
            while j * L <= m:
                left = j * L
                right = min(m, (j + 1) * L - 1)
                if j < P:
                    cur += j * (pref[right] - pref[left - 1])
                elif j > P:
                    cur += (P - 1) * (pref[right] - pref[left - 1])
                else:
                    cnt = pref[right] - pref[left - 1]
                    cur += (P - 1) * cnt
                    if left <= m:
                        cur += freq[left]
                j += 1
            if cur > maxcur:
                maxcur = cur
        ans[kk] = maxcur
    
    for k in range(LIM + 1, m + 1):
        ans[k] = maxfull
    
    for k in range(2, m + 1):
        if ans[k] < ans[k - 1]:
            ans[k] = ans[k - 1]
    
    print(' '.join(map(str, ans[1:])))