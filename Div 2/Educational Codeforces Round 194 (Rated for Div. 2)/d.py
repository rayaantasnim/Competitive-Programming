import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    qrTNum = int(data[0])
    idx = 1
    
    out = []
    for _ in range(qrTNum):
        n = int(data[idx])
        s = data[idx+1].strip()
        idx += 2
        
        if s[0] == '0' or '00' in s:
            out.append("-1")
            continue
            
        low, high, ans = 1, n, -1
        while low <= high:
            mid = (low + high) // 2
            possible = True
            intervals = [(0, 0)]
            
            for ch in s:
                nxt = []
                for l, r in intervals:
                    if l == r:
                        nxt.append((l - mid, l - 1))
                        nxt.append((l + 1, l + mid))
                    else:
                        nxt.append((l - mid, r + mid))
                
                nxt.sort(key=lambda x: (x[0], x[1]))
                
                if ch == '+':
                    L, R = 1, 2 * 10**18
                elif ch == '-':
                    L, R = -2 * 10**18, -1
                else:
                    L, R = 0, 0
                    
                merged = []
                for l, r in nxt:
                    cl, cr = max(l, L), min(r, R)
                    if cl <= cr:
                        if merged and cl <= merged[-1][1] + 1:
                            if cr > merged[-1][1]:
                                merged[-1] = (merged[-1][0], cr)
                        else:
                            merged.append((cl, cr))
                            
                if not merged:
                    possible = False
                    break
                intervals = merged
                
            if possible:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
