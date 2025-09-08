def task_1_tuple(x, y):
    tpl = []
    for i in range(x, y+1):
        tpl += tuple((i, ))
    return tuple(sorted((tpl)))

def task_2_tuple(x, y):
    tpl1 = ('car1', 'car2', x, 'car4', 'car5')
    tpl2 = tpl1[:2] + (y, ) + tpl1[3:]
    return tpl2

def task_3_tuple(x, y):
    print(x)
    print(y)
    print()
    x, y = y, x
    print(x)
    print(y)
    