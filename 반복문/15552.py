import sys

the_number_of_testcase_T = int(input())
for i in range(the_number_of_testcase_T) :
  A, B = map(int,sys.stdin.readline().split())
  print(A + B)

the_number_of_testcase_T = int(input())
for i in range(the_number_of_testcase_T) :
  print(sum(map(int,sys.stdin.readline().split())))
