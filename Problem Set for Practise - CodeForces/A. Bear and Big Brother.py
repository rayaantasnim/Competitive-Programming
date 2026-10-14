a, b = map(int, input().split())
years = 0

# কন্ডিশনটি হবে: যতক্ষণ a ছোট বা সমান b
while a <= b:
    a *= 3
    b *= 2 
    years += 1

print(years)
