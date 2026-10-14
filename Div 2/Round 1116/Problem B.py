t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    
    odd_p0 = True
    odd_p1 = True
    for i in range(0, n, 2):
        pos = i // 2

        if (s[i] == '0'):
            if (pos % 2 == 0):
                odd_p1 = False

            else:
                odd_p0 = False

        elif (s[i] == '1'):
            if (pos % 2 == 0):
                odd_p0 = False
            else:
                odd_p1 = False
                
    if (odd_p0 and odd_p1):
        odd_ways = 2

    elif (odd_p0 or odd_p1):
        odd_ways = 1
        
    else:
        odd_ways = 0
        
    even_p0 = True
    even_p1 = True
    for i in range(1, n, 2):
        pos = (i - 1) // 2

        if (s[i] == '0'):
            if (pos % 2 == 0):
                even_p1 = False
            else:
                even_p0 = False

        elif (s[i] == '1'):
            if (pos % 2 == 0):
                even_p0 = False
            else:
                even_p1 = False
                
    if (even_p0 and even_p1):
        even_ways = 2

    elif (even_p0 or even_p1):
        even_ways = 1

    else:
        even_ways = 0
        
    print((odd_ways * even_ways) % 998244353)
