def new_list():
    newlist={
        "elements": [],
        "size": 0,
        }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexit = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexit = True
                break
        if keyexit:
            return keypos
    return -1