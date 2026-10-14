n = int(input())
array = list(map(int,input().split()))
upgraded_list = [0] * n

for i in range(n):
    giver = i + 1          # যে গিফট দিচ্ছে (যেহেতু ইনডেক্স ০ থেকে শুরু, তাই ১ যোগ করলাম)
    receiver = array[i]    # যে গিফট পাচ্ছে
    upgraded_list[receiver - 1] = giver

print(*upgraded_list)
