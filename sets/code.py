def task_1_set(set_super, set_1, set_2):
    print(set_super >= set_1) 
    print(set_super >= set_2) 
    print(set_super.issuperset(set_1))
    print(set_super.issuperset(set_2))

    # set_super - чистое супермножество только для set_2
    # Так как set_super имеет большую мощность, чем у set_2
    print(set_super > set_1) 
    print(set_super > set_2) 
def task_2_set(lst):
    set_1 = set()
    new_lst = []

    for el in lst:
        povt = new_lst.count(el)
        if povt == 0:
            set_1.add(el)
        else:
            set_1.add(str(el) * (povt + 1)) 
        new_lst.append(el)

    print(set_1)
def task_3_set(lst_1, lst_2):
    set_1 = set(lst_1)
    set_2 = set(lst_2)
    print(set_1.intersection(set_2))
def task_4_set(x):
    lst = list(map(int, x.split()))
    # lst = [1, 2, 1, 3, 3, 2, 4]
    print(lst)
    new_lst = []

    for i in lst:
        if i in new_lst:
            print("YES", end=" ")
        else:
            new_lst.append(i)
            print("NO", end=" ")

        print(new_lst)
def task_5_set(set_1, lst):
    set_1.update(lst)  # Работает в режиме in-place
    print(set_1)