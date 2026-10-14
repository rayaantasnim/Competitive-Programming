import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    is_valid = [True] * n
    for i, ak in enumerate(a):
        k = i + 1        
        L = ak * k
        R = (ak + 1) * k
        
        if L < n:
            end = min(n, R)
            for y in range(L, end):
                is_valid[y] = False
                
    ans = [y for y in range(n) if is_valid[y]]
    
    print(len(ans))
    print(*ans)

def main():
    for _ in range(int(input())):
        solve()

if __name__ == '__main__':
    main()
