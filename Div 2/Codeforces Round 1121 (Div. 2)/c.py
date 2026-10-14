import sys

def main():
    MOD = 998244353

    line = sys.stdin.readline()
    if not line:
        return
    t = int(line.strip())
    
    for _ in range(t):
        line = sys.stdin.readline()
        if not line:
            break
        n = int(line.strip())
        
        line = sys.stdin.readline()
        if not line:
            break
        a = list(map(int, line.strip().split()))
        
        if len(set(a)) != n:
            print(-1)
            continue
            
        if n == 1:
            print(0)
            continue
            
        a.sort()
        
        total_trees = 1
        for i in range(1, n):
            total_trees = (total_trees * i) % MOD
            
        ans = 0
        s = 0
        
        for i in range(n - 1, -1, -1):
            k = n - 1 - i
            if k > 0:
                diff = (s - k * a[i]) % MOD
                ways = (total_trees * pow(k, MOD - 2, MOD)) % MOD
                ans = (ans + diff * ways) % MOD
            s = (s + a[i]) % MOD
            
        print(ans)

if __name__ == '__main__':
    main()
