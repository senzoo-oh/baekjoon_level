T = int(input())    # 테스트 케이스 수
for i in range(T) :
    k = int(input())    # 층
    n = int(input())    # 호

    apartment = []

    # 0층을 만듦.
    floor_0 = []
    for i in range(1, n + 1) :
        floor_0.append(i)
    apartment.append(floor_0)
    current = floor_0

    # 윗층을 만듦.
    for i in range(k) :
        next = []
        for j in range(1, n + 1) :
            num = sum(current[:j])
            next.append(num)
        current = next
        apartment.append(current)

    print(apartment[k][n-1])

# for i in range(k+1) :
#     for j in range(n) :
#         print(apartment[i][j], end = ' ')
#     print()