import sys

def task_4(dict_4, key):
    if key in dict_4:
        print(f'{key} exists in the dictionary')
    else:
        print(f'{key} does not exist in the dictionary')

if __name__ == "__main__":
    # Extract key from command line
    key = sys.argv[1]
    dict_4={'value1': 1, 'value2': 2, 'value3': 3,"value4":8}
    # Call the function with the dictionary and key
    task_4(dict_4, key)
