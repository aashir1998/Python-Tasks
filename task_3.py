def task_3(arr):
    dict3 = {key: value for key, value in arr.items() if value % 2 == 0}
    print(dict3)


task_3({"value1": 1, "value2": 2, "value3": 3, "value4": 8})
