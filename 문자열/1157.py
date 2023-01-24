from collections import Counter

word = input().upper()
list = Counter(word).most_common()
if len(list) == 1:
    print(list[0][0])
elif list[0][1] == list[1][1] :
    print("?")
else :
    print(list[0][0])