num = int(input())

while num != 0 :
    count = 2 * num + 1
    number = [True] * (count)
    for i in range(2, count) :
        if number[i] == True :
            for j in range(i + i, count, i) :
                number[j] = False
    prime = [i for i in range (num + 1, count) if number[i] == True]
    print(len(prime))
    num = int(input())

