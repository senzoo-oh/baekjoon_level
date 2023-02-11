A, B = [], []

# 9 * 9 배열 만들고, 숫자 입력받기.
for i in range(9) :
    nums = list(map(int,input().split()))
    A.append(nums)

# sublist의 최댓값들로 리스트 B 만들기.
for i in range(9) :
    sublist = A[i]
    max_number_in_sublist = max(sublist)
    B.append(max_number_in_sublist)

# 리스트 B에서 최댓값 출력.
print(max(B))

# 리스트 A 에서 최댓값 좌표 출력.
x = B.index(max(B))
print(x+1, A[x].index(max(B))+1)