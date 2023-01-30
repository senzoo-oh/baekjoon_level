N = int(input())
num_of_bag = 0

while N >= 0 :
    if N % 5 == 0 :
        num_of_bag += (N//5)
        print(num_of_bag)
        break
    N -= 3
    num_of_bag += 1
else :
    print(-1)