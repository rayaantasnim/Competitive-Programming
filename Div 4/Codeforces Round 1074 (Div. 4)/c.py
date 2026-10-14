for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    unique = sorted(list(set(a)))

    max_streak = 1
    current_streak = 1

    for i in range(1, len(unique)):
        if unique[i] == unique[i - 1] + 1:
            current_streak += 1
            
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 1

    max_streak = max(max_streak, current_streak)

    print(max_streak)
