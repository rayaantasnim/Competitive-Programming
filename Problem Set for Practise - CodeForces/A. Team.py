solved_count = 0
for i in range(int(input())):
    p, v, t = map(int, input().split())
    if(p + v + t>1):
        solved_count +=1 

print(solved_count)