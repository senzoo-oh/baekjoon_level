white_paper = [([0] * 100) for i in range(100)]
number_of_black_paper = int(input())

for i in range(number_of_black_paper) :
    x, y = map(int,input().split())
    for i in range(x, x + 10) :
        for j in range(y, y + 10) :
            white_paper[i][j] = 1

area = 0
for i in range(100) :
    area += sum(white_paper[i])
print(area)