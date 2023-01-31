N = int(input())
num = list(map(int,input().split()))
count = 0

for i in num :
    if i == 1 :                 # 1 제외
        continue
    elif i == 2 :               # 2는 소수
        count += 1
        continue
    for j in range(2, i) :      # 3이상 수부터 판별
        if i % j == 0 :
            break
    else :
        count += 1      
# i % j == 0이 사실이 아닐때 else문이 실행됨. 즉, break문을 만나면 실행이 되지 않음.

print(count)