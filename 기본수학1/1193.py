X = int(input())

point = 1               # 꺾이는 부분(1, 2, 4, 7, 11...)
point_count = 1         # 꺽이는 부분의 증가값
line = 0                # 몇번째 줄

while True :            # 몇번째 줄 인지 계산
    if (X < point) :
        break
    else :
        point += point_count
        point_count += 1
        line += 1

count = X - (point - point_count)   # 몇번째 칸
if line % 2 == 0 :      # 짝수일때
    print(f"{count}/{(line+1)-count}")
else :                  # 홀수일때
    print(f"{(line+1)-count}/{count}")