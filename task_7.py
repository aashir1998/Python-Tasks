def reverse_dict(dictt):
    reversed_dict = {value: key for key, value in dictt.items()}
    return reversed_dict

dictt = {'value1': 1, 'value2': 2, 'value3': 3}
print(reverse_dict(dictt))