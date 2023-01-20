import sys
C = int(input())

for i in range(C) :
  num = list(map(int,sys.stdin.readline().split()))
  N = num[0]
  average = sum(num[1:])/N
  good_student = 0
  for i in num[1:] :
    if average < i :
      good_student += 1
  rate = good_student / N * 100 
  print("%.3f" % rate + "%")