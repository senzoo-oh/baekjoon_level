the_number_of_test_case = int(input())
for i in range(the_number_of_test_case) :
  quiz_result = list(input())
  count = 0
  sum = 0
  for result in quiz_result :
    if result == 'O' :
      count += 1
      sum += count
    else :
      count = 0
  print(sum)