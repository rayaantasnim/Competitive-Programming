x = 0 
for i in range(int(input())):
    bit = input()
    if("+" in bit):
        x +=1 

    elif("-" in bit):
        x -=1
print(x)