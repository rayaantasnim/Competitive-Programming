# প্রথমে খালি একটি ম্যাট্রিক্স (লিস্টের ভেতর লিস্ট) নেব
matrix = []

# ৫টি লাইনের ইনপুট নিয়ে ম্যাট্রিক্সে যোগ করব
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# এবার পুরো ৫টি লিস্ট আসার পর আমরা লুপ চালিয়ে ১-কে খুঁজব
for r in range(5):
    for c in range(5):
        # যদি ১ খুঁজে পাই
        if matrix[r][c] == 1:
            # পাইথনে ইনডেক্স ০ থেকে শুরু হয়, তাই মানুষের গণনার (১ থেকে ৫) সাথে মেলাতে ১ যোগ করব
            row_position = r + 1
            col_position = c + 1
            
            # মাঝখানের ঘর (৩, ৩) থেকে দূরত্ব বা চালের সংখ্যা বের করব
            moves = abs(row_position - 3) + abs(col_position - 3)
            
            # চূড়ান্ত উত্তর প্রিন্ট করব
            print(moves)
            break
