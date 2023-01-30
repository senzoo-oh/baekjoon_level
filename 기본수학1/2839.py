N = int(input())
num_3 = 0       # 3kg 봉지의 개수

while True :
    num_5 = (N - (3 * num_3)) / 5   # 5kg 봉지의 개수
    if (N - (3 * num_3)) % 5 == 0 :
        number_of_bag = int(num_3 + num_5)
        print(int(number_of_bag))
        break
    elif num_5 < 1 :                
        if N % 3 == 0 :
            print(N // 3)
            break
        else :
            print(-1)
            break
    else :
        num_3 +=1