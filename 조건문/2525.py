A, B = map(int, input().split())
C = int(input())

M = B + C

if M >= 60 :
  while (M >= 60) :
    M = M - 60
    A = A + 1
    if A == 24 :
      A = 0
  print(A, M, end ='')
else :
    print(A, M, end ='')
