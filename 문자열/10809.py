# list = [-1 for x in range(ord('a'),ord('z')+1)]
# S = str(input())

# for ch in S :
#     for i in range(ord('a'),ord('z')+1) :
#         if ord(ch) == i :
#             if list[i - 97] == -1 :
#                 list[i - 97] = S.index(ch)
# for i in range(len(list)) :
#     print(list[i],end = ' ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
S = input()

for i in alphabet :
    print(S.find(i))