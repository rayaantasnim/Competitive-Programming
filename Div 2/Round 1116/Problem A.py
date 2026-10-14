t = int(input())

for i in range(t):
    array = list(map(int, input().split()))
    array.sort()

    add = array[0] + array[1]
    if(add < array[2]):
        add, array[2] = array[2], add
    print(array[2]-array[0])