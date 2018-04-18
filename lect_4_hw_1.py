def song(string=3, l=3, p=0):
    la_in_string = ["la"] * l
    separator = "-"
    ready_string = separator.join(la_in_string)
    ready_song = [ready_string] * string
    new_line = "\n"
    strings = new_line.join(ready_song)
    if p == 0:
        strings = strings + "."
    elif p == 1:
        strings = strings + "!"
    return strings


print(song(5, 7, 20))

