for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ones = a.count(1)

    if ones >= (n + 1) // 2:
        print("Bessie")
    else:
        print("Elsie")
