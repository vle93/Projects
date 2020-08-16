#This program will reverse an example string and print it out.

def main(string):
    reverse_string = ""
    num = len(string) - 1
    for i in string:
        reverse_string += string[num]
        num -= 1
    return reverse_string

print(main("Hello World"))