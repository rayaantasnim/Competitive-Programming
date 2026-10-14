t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total_sum = sum(a)
    odd_numbers = []

    for x in a:
        if x % 2 != 0:
            odd_numbers.append(x)

    if len(odd_numbers) == 0:
        print(0)
    else:
        odd_numbers.sort()
        how_many_to_remove = len(odd_numbers) // 2
        ans = total_sum - sum(odd_numbers[:how_many_to_remove])
        print(ans)
