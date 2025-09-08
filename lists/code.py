def task_1_list(x, y):
    lst = []
    
    for i in range(x, y+1):
        
        lst.append(i)
        
    return lst

def task_2_list(a, b, c, d, e, f, g):
    lst = [a, b, c, d, e, f, g]
    lst = [el-100 if el >= 175 else el ** 0.5 for el in lst]
    return lst

def task_3_list(a, b, c, d, e, f, g):
    lst = [a, b, c, d, e, f, g]
    lst = [el * 12 if el > 5 and el <= 10 else el * 3 if el > 11 and el <= 16 else el + 12 if el > 16 and el <= 20 else el for el in lst]
    return lst

def task_4_list(x, y):
    lst = [[i for i in range(x, y+1)] for _ in range(7)]
    return lst

def task_5_list(x):
    lst = x[0:round(len(x)/2)]
    lst1 =  x[round(len(x)/2):]
    print(lst)
    print(lst1)