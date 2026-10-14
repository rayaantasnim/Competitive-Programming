test = int(input())

for i in range(test):
    n = int(input())
    a = n+1

    if(a<2):
        result = "NO"

    elif(a==2):
        result = "YES"

    elif(a%2==0):
        result = "NO"

    else:
        result = "YES"
        for i in range(3, a, 2):
            if(a%i==0):
                result = "NO"
                break

    print(result)