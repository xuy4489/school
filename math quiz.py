import random


# checks users enter  yes (y) or no (n)
def yes_no(response):
    while True:
        response = input(response).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''

     **** Instructions ****

First, the system will give you addition, subtraction
multiplication and division within 10, and you cannot use a calculator.

But I hope you can try to use mental arithmetic
Because addition and subtraction within 10 are relatively simple.

Of course, I don't mind you using a computer.
But if you use a calculator, then this game will be useless

Good luck.

     ''')


# Main routine
print()
print("🧊🧊🧊 Welcome to the Higher Lower Game 🔻🔻🔻")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to read instructions? ")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

count = 0
right = 0
exitcode= True
while exitcode:
    a = random.randint(0, 9)
    b = random.randint(1, 9)
    op = ['+', '-', '*']
    d = random.choice(op)
    print('%d %s %d = ' % (a, d, b))
    print('')
    result1 = a + b
    result2 = a - b
    result3 = a * b
    while True:
        print('Please enter your answer：(Press q to exit) ')
        question = input()
        if question=="q":
            exitcode=False
            break
        try:
            question = int(question)
            break
        except ValueError:
            print("Please input an integer")

    if question == result1 and d == '+':
        print('correct answer')
        right += 1
        count += 1
    elif question == result2 and d == '-':
        print('correct answer')
        right += 1
        count += 1
    elif question == result3 and d == '*':
        print('correct answer')
        right += 1
        count += 1
    else:
        print('wrong answer')
        count += 1

percent = right / count
print('The test is over. A total of %d questions were answered, %d '
      'were answered correctly, and the correct rate was '
      '%d. 2f%%'
      % (count, right, percent * 100))
