T = int(input())
import sys
for i in range(T):
    H, W, N = map(int,sys.stdin.readline().split())

    hotel = []
    for i in range(H) :
        hotel.append([])
        for j in range(W) :
            floor = str(i + 1)
            distance = str(j+1)
            room_number = floor + distance.zfill(2)
            hotel[i].append(room_number)
    if (N%H) == 0 :
        b = N//H -1
    else :
        b = N//H
    print(hotel[N-(H*(N//H))-1][b])