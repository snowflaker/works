def pre_min(*args):
    list_values = list(args)
    list_values.sort()

    for f in list_values[1:]:
        if list_values[0] != f:
            print(f)
            break


pre_min("a", "a", "b", "aak")