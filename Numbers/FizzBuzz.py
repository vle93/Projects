#This program prints the numbers from 1 to 100.
#It will print: "Fizz" for multiples of 3
#               "Buzz" for multiples of 5
#               "FizzBuzz" for mutliples of both 3 and 5

def main():
    for i in range(1, 101):
        if(i % 3 == 0):
            if(i % 5 ==0):
                print("FizzBuzz")
            else:
                print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    main()