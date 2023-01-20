N = int(input())
grade = list(map(int,input().split()))
M = max(grade)
manipulated_grade = [item / M * 100 for item in grade]
print(sum(manipulated_grade)/len(manipulated_grade))