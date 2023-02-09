N, M = map(int,input().split())

def make_list(N, M) :
    nested_list = [[] for _ in range(N)]
    for i in range(N) :
        nums = list(map(int,input().split()))
        nested_list[i] = nums
    return nested_list

A = make_list(N, M)
B = make_list(N, M)

for i in range(N) :
    for j in range(M) :
        print(A[i][j] + B[i][j],end = ' ')
    print()