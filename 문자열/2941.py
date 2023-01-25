word = input()
croatia_alphabet = ['dz=','c=','c-','d-','lj','nj','s=','z=']

for croatia in croatia_alphabet :
    word = word.replace(croatia,'1')

print(len(word))