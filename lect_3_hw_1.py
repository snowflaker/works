# exercise3_1
word = input()
try:
    print(
    word[2],
    word[-2],
    word[:5],
    word[:-2],
    word[::2],
    word[1::2],
    word[::-1],
    word[-2:0:-1],
    word[0:5],
    len(word),
    sep="\n")
except IndexError as e:
    print(e)