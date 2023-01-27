# A = 고정비용(임대료, 재산세, 보혐료, 급여)
# B = 가변비용(재료비, 인건비)
# C = 노트북의 가격
# 총 수입 = c
# 총 비용 = A(고정비용) + B(가변비용) = A + (B * 생산대수)
# 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점
# 손익분기점을 구하는 프로그램
# 노트북 한대당 수익 = (C - B)

A, B, C = map(int,input().split())

if (B >= C) :
    print("-1")
else :
    n = A/(C-B)
    print(int(n+1))
