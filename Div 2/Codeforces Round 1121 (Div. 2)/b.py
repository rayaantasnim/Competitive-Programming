import sys
import heapq

def solve():
    input_line = sys.stdin.readline
    t_str = input_line()
    if not t_str:
        return
    t = int(t_str)
    
    for _ in range(t):
        n_m = input_line()
        if not n_m:
            break
        n, m = map(int, n_m.split())
        a = list(map(int, input_line().split()))
        
        if m == 1:
            print(max(a))
            continue
            
        hp = []
        current_sum = 0
        max_score = -float('inf')
        
        for j in range(n):
            if len(hp) == m - 1:
                score = m * a[j] - current_sum
                if score > max_score:
                    max_score = score
                    
            if len(hp) < m - 1:
                heapq.heappush(hp, -a[j])
                current_sum += a[j]
            else:
                if a[j] < -hp[0]:
                    top = -heapq.heappop(hp)
                    current_sum -= top
                    heapq.heappush(hp, -a[j])
                    current_sum += a[j]
                    
        print(max_score)

if __name__ == '__main__':
    solve()
