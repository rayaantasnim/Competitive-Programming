n = int(input())
s = input().lower()
print("Anton" if s.count("a") > s.count("d") else "Danik" if s.count("a") < s.count("d") else "Friendship")
