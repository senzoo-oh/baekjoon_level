import sys
for i in range(int(input())) :
    H, W, N = map(int,sys.stdin.readline().split())
    floor = N - (H * ((N - 1) // H))
    distance = str((N - 1) // H + 1)
    print(floor,distance.zfill(2), sep='')