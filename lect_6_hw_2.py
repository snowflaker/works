f = open("lect_6_hw_1.py")
w = open("write_hw_1", "w")
number = 0
for line in f:
    number = number + 1
    print(number, ":", line, file=w)
f.close()
w.close()


with open("lect_6_hw_1.py") as f, open("write_hw_2", "w") as w:
    number = 0
    for line in f:
        number = number + 1
        string = str(number) + ":" + line
        w.write(string)


