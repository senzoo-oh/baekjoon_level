N = int(input())
home = 2
i = 1

while True :
    if N < home :
        print(i)
        break
    else :
        home += (6*i)
        i += 1

