t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 0 or k > 2*n:
        print(-1)
        continue
    # build matrix
    A = [[0]*n for _ in range(n)]
    num = 1
    # put 1..n in first column
    for i in range(n):
        A[i][0] = num
        num += 1
    # put extra (k-n) numbers in first row
    extra = k - n
    for j in range(1, extra+1):
        A[0][j] = num
        num += 1
    # fill rest arbitrarily
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:
                A[i][j] = num
                num += 1
    for row in A:
        print(*row)
