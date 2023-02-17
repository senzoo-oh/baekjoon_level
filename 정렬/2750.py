N = int(input())
array = []

for i in range(N):
    i = int(input())
    array.append(i)
array.sort()
for i in array:
    print(i)