y = str(int(input()) +1)
while(True):
    if(len(set(y))==4):
        print(y)
        break 
    else:
        y = str(int(y) + 1)