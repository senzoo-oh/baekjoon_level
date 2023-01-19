import sys
the_number_of_testcase_T = int(input())

for i in range(1, the_number_of_testcase_T+1) :
  print("Case #",i,": ",sum(map(int,sys.stdin.readline().split())),sep='')
