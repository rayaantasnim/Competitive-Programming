import sys

def solve():
    l = sys.stdin.readline
    t_str = l()
    if not t_str:
        return
    t = int(t_str)
    
    for _ in range(t):
        n = int(l())
        
        if n == 1:
            print("1")
        elif n == 2:
            print("11")
        elif n == 3:
            print("101")
        elif n == 4:
            print("0101")
        elif n == 5:
            print("10101")
        elif n == 6:
            print("010100")
        elif n == 7:
            print("0010100")
        elif n == 8:
            print("10010100")
        else:
            rem = (n - 9) % 6
            q = (n - 9) // 6
            
            if rem == 0:
                b = [2 + 2*q, 3 + 2*q, 2 + 2*q]
            elif rem == 1:
                b = [2 + 2*q, 3 + 2*q, 3 + 2*q]
            elif rem == 2:
                b = [3 + 2*q, 3 + 2*q, 3 + 2*q]
            elif rem == 3:
                b = [3 + 2*q, 3 + 2*q, 4 + 2*q]
            elif rem == 4:
                b = [4 + 2*q, 3 + 2*q, 4 + 2*q]
            else:
                b = [0, 4 + 2*q, 3 + 2*q, 4 + 2*q]
                
            if len(b) == 3:
                ans = '0' * b[0] + '1' + '0' * b[1] + '1' + '0' * b[2]
            else:
                ans = '0' * b[0] + '1' + '0' * b[1] + '1' + '0' * b[2] + '1' + '0' * b[3]
            print(ans)

if __name__ == '__main__':
    solve()
