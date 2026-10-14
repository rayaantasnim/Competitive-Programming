import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    t = int(data[0])
    p = int(data[1])
    
    queries = [int(x) for x in data[2:]]
    max_n = 400
    
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = (fact[i-1] * i) % p
        
    A = [0] * (max_n + 1)
    A[1] = 1
    if max_n >= 2:
        A[2] = 2
    if max_n >= 3:
        A[3] = 0
        
    E = [0] * (max_n + 1)
    E[1] = 1
    if max_n >= 2:
        E[2] = 1
        
    for n in range(4, max_n + 1):
        total = fact[n]
        
        sum1 = 0
        for k in range(2, n):
            sum1 = (sum1 + A[k] * fact[n - k + 1]) % p
            
        sum2 = 0
        for k in range(3, n):
            sum2 = (sum2 + E[k] * fact[n - k + 1]) % p
            
        A[n] = (total - sum1 - 2 * fact[n - 1] + sum2) % p
        A[n] = (A[n] + p) % p
        
        E_sum = 0
        for k in range(2, n):
            E_sum = (E_sum + A[k] * E[n - k + 1]) % p
        E[n] = (A[n] + E_sum) % p
        
    out = []
    for n in queries:
        out.append(str(A[n]))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
