
def color_filter():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    x = color_list_1.difference(color_list_2)
    return x

print(color_filter())