number = input()
lucky = number.count("4") + number.count("7")
print("YES" if (lucky==4 or lucky==7) else "NO")