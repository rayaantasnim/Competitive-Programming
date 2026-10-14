import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        h = int(data[idx + 2])
        idx += 3
        
        a = [int(x) for x in data[idx:idx + n]]
        idx += n
        
        v = a[:]
        w = [-1] * n
        last_reset = 0
        
        for p in range(1, m + 1):
            b = int(data[idx]) - 1
            c = int(data[idx + 1])
            idx += 2
            
            if w[b] < last_reset:
                v[b] = a[b]
                
            w[b] = p
            v[b] += c
            
            if v[b] > h:
                v[b] = a[b]
                last_reset = p
                
        ans = []
        for p in range(n):
            if w[p] > last_reset:
                ans.append(str(v[p]))
            else:
                ans.append(str(a[p]))
                
        out.append(" ".join(ans))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()
