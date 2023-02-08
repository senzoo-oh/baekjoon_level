N = int(input())
i = 2
while N / i != 1.0 :
    if N % i == 0 :
        print(i)
        N = int(N/i)
    else :
        i += 1
print(i)

