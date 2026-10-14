import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    
    temp = n
    p = -1
    q = -1
    
    i = 2
    while i * i <= temp:
        if temp % i == 0:
            p = i
            while temp % i == 0:
                temp //= i
            break
        i += 1
        
    if temp > 1:
        if p == -1:
            p = temp
        else:
            q = temp
            
    if p == -1 or q == -1:
        print("NO")
        return
        
    for a2 in range(1, p):
        rem = n - 1 - a2 * q
        if rem % p == 0:
            a1 = rem // p
            if a1 > 0:
                b1 = n // p
                b2 = n // q
                print("YES")
                print(2)
                print(f"{a1} {b1}")
                print(f"{a2} {b2}")
                return

    print("NO")

if __name__ == '__main__':
    solve()
