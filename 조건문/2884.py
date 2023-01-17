H, M = map(int, input().split())

if (M - 45) < 0 :
  if H == 0 :
    H = 24 - 1
  else :
    H = H - 1
  M = M + 60
  M = M - 45
  print(H, M, end = '' )
else :
  M = M - 45
  print(H, M, end = '' )