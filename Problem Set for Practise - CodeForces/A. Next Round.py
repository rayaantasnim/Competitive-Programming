n, k = map(int, input().split())
scores = list(map(int, input().split()))
target_score = scores[k - 1]
count = 0

for a in scores:
    if(a>0 and a>=target_score):
        count +=1
print(count)