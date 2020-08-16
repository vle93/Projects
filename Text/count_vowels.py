#This program will count the vowels in a string

def main():
    string1 = "THIS SENTENCE has 7 vowels"
    vowels = ['a', 'e', 'i', 'o', 'u']
    string_lower = string1.lower()
    vowel_count = 0

    print(string_lower)

    for char in string_lower:
        for vowel in vowels:
            if char == vowel:
                vowel_count += 1
    return vowel_count

print(main())