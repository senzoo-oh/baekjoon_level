def hansu(num) :
    count = 0
    for i in range (1,num+1) :
        if i < 100 :
            count += 1
            continue
        hundredth = i//100
        tenth = (i//10)%10
        ones = i%10
        if (hundredth - tenth) == (tenth - ones) :
            count += 1
    return count
N = int(input())
print(hansu(N))