word = input()

up = 0
low = 0

for a in word:
    if(a.islower()):
        low +=1
    else:
        up+=1
print(word.upper() if(low<up) else word.lower())