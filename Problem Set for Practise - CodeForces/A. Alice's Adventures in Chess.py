for i in range(int(input())):
    n,a,b = map(int,input().split())
    s = input()

    x = y = 0 
    result="NO"

    for loop in range(30):
        for j in s:

            if(j=="N"):
                y+=1
                
            elif(j=="E"):
                x+=1

            elif(j=="S"):
                y-=1

            elif(j=="W"):
                x-=1

            if(a==x and b==y):
                result="YES"
                break
            else:
                continue
            
        if(result=="YES"):
            break
    
    print(result)