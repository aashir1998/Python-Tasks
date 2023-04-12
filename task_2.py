def task_2(my_dict1, my_dict2):
    dict3 = my_dict1.copy()
    dict3.update(my_dict2)
    for key in my_dict1:
        if key in my_dict2:
            dict3[key] = my_dict1[key] + my_dict2[key]
    print(dict3)


my_dict1 = {1: 100, 2: 200, 3: 300}
my_dict2 = {1: 100, 5: 200, 9: 300}
task_2(my_dict1, my_dict2)
