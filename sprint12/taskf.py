string = input()
only_alpha = ""

for char in string:
    if ord(char) >= 65 and ord(char) <= 90:
        only_alpha += char.lower()
    elif ord(char) >= 97 and ord(char) <= 122:
        only_alpha += char

sentence = only_alpha[::-1]

print(sentence == only_alpha)
