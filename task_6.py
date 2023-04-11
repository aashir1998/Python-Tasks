import sys

def reverse_words(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


if __name__ == '__main__':
    string = sys.argv[1]
    reversed_string = reverse_words(string)
    print(reversed_string)