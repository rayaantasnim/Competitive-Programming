import sys

def solve():
    MAXN = 3005
    rad = [1] * MAXN
    pt = [True] * MAXN
    for i in range(2, MAXN):
        if pt[i]:
            for j in range(i, MAXN, i):
                pt[j] = False
                rad[j] *= i

    MOD = 998244353
    pow2 = [1] * MAXN
    for i in range(1, MAXN):
        pow2[i] = (pow2[i - 1] * 2) % MOD

    V = [MAXN] * MAXN
    for x in range(1, MAXN):
        for y in range(x + 1, MAXN):
            if x % rad[y] == 0:
                V[x] = y - 1
                break

    line = sys.stdin.readline()
    if not line:
        return
    t = int(line.strip())

    for _ in range(t):
        while True:
            line = sys.stdin.readline()
            if not line:
                return
            parts = line.split()
            if parts:
                n = int(parts[0])
                break
        
        a = []
        while len(a) < n:
            line = sys.stdin.readline()
            if not line:
                return
            a.extend(map(int, line.split()))
        
        if any(x < 1 or x > n for x in a):
            print(-1)
            sys.stdout.flush()
            return

        max_x = [[0] * (n + 1) for _ in range(n + 1)]
        for x in range(1, n + 1):
            vx = V[x]
            if vx > n:
                vx = n
            for L in range(x, n + 1):
                for R in range(L, vx + 1):
                    if x > max_x[L][R]:
                        max_x[L][R] = x

        cnt = [0] * (n + 1)
        for x in a:
            cnt[x] += 1

        ans = 0
        for L in range(1, n + 1):
            if cnt[L] == 0:
                continue
            
            ways = (pow2[cnt[L]] - 1) % MOD
            ans = (ans + ways * max_x[L][L]) % MOD
            
            mid_ways = 1 
            for R in range(L + 1, n + 1):
                if cnt[R] > 0:
                    ways = (pow2[cnt[L]] - 1) * (pow2[cnt[R]] - 1) % MOD
                    ways = (ways * mid_ways) % MOD
                    ans = (ans + ways * max_x[L][R]) % MOD
                    mid_ways = (mid_ways * pow2[cnt[R]]) % MOD

        print(ans)
        sys.stdout.flush()

if __name__ == '__main__':
    solve()
