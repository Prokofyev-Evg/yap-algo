import sys

length = int(input())
sentence = sys.stdin.readline().rstrip().split()

max_size = 0
max_word = ""

for i in range(len(sentence)):
    if max_size < len(sentence[i]):
        max_size = len(sentence[i])
        max_word = sentence[i]

print(max_word)
print(max_size)
