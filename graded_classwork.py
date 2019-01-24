def main():
    # problem1()
    # problem2()
    problem3()

#counts from 0-10 using a for loop and range function
def problem1():
    for x in range(0,10):
        print(x)



def problem2():
    userInput = ""
    while userInput != 'q':
        userInput = input("press the correct letter!")

def problem3():

    num1 = int(input("Pick a number?"))
    num2 = int(input('pick another number'))

    print(num1 + num2)



# def add():
#
# def subtract():
# def multiply():
# def divide():


if __name__ == '__main__':
    main()
