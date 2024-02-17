# zero

# import package
import random as ran

# universe variables
exitstr = ['exit()', 'exit', '0']
editstr = 'edit()'
nextstr = 'next()'
backstr = 'back()'
helpstr = 'help()'
exitsms = 'and You are logged out, good luck.'
invalidsms = 'Invalid Answer, Please enter a number.'
byebyesms = 'Good luck, Bye.'
problem = 'there is problem in'
error = 'Error Code'
# C c Cou cou is Counter
# _ i I j J for Loops (for, while)

# Global Variables
score = int(0)

selectsms = 'You Selected:'
notselectedsms = "You haven't selected any mode,"

practicesms = '1. Practice Mode'
gamesms = '2. Game Mode'

plussms = '1. Plus Mode'
minussms = '2. Minus Mode'
timessms = '3. Times Mode'
divisionsms = '4. Division Mode'

easysms = '1. Easy Mode'
mediumsms = '2. Medium Mode'
hardsms = '3. Hard Mode'

'''

*** Errors answer ***
Code 9: How did you get this error? You are a legend.

'''
def UserName():
    global username
    while True:
        username = str(input('Enter Your Name: '))
        if username:
            print(f'Hello {username}')
            MathGame()
        else:
            x = 5 + 5
def UserScore(scorepoint):
    global score
    if scorepoint == '+':
        score = score + 2
    elif scorepoint == '-':
        score = score - 1
    return score

def RandomNum():
    num1 = ran.randint(1,10)
    num2 = ran.randint(1,10)
    return num1, num2

def CalculateNum(num1,oprator,num2):
    if oprator == '+':
        correct_answer = num1 + num2
        return correct_answer
    elif oprator == '-':
        correct_answer = num1 - num2
        return correct_answer
    elif oprator == '*':
        correct_answer = num1 * num2
        return correct_answer
    elif oprator == '/':
        correct_answer = num1 / num2
        return correct_answer
    else:
        print('Unknown Problem.(CalculateNum)')
        exit()
def CalculateRan(game_mode):
    num1, num2= RandomNum()
    if game_mode == 'easy':
        oprator = ran.choice(['+','-'])
        if oprator == '+':
            correct_answer = num1 + num2
        elif oprator == '-':
            correct_answer = num1 - num2
        else:
            print('Unknown Problem.(CalculateRan easy)')
            exit()
    elif game_mode == 'medium':
        oprator = ran.choice(['+','-','*'])
        if oprator == '+':
            correct_answer = num1 + num2
        elif oprator == '-':
            correct_answer = num1 - num2
        elif oprator == '*':
            correct_answer = num1 * num2
        else:
            print('Unknown Problem.(CalculateRan medium)')
            exit()
    elif game_mode == 'hard':
        oprator = ran.choice(['+','-','*', '/'])
        if oprator == '+':
            correct_answer = num1 + num2
        elif oprator == '-':
            correct_answer = num1 - num2
        elif oprator == '*':
            correct_answer = num1 * num2
        elif oprator == '/':
            correct_answer = num1 / num2
        else:
            print('Unknown Problem.(CalculateRan hard)')
            exit()
    else:
        print('Unknown Problem.(CalculateRan)')
        exit()
    return oprator, correct_answer, num1, num2

def PluseMode():
    while True:
        num1, num2 = RandomNum()
        correct_answer = CalculateNum(num1,'+',num2)
        try:
            user_answer = input(f'{num1} + {num2} = ')
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                print("It's true")
                UserScore(scorepoint = '+')
            elif user_answer != correct_answer:
                print(f"Not True, The Correct Answer is {correct_answer}")
                UserScore(scorepoint = '-')
            else:
                print(invalidsms)
        except ValueError:
            if user_answer in exitstr:
                print(f'Your Score: {score}')
                print(byebyesms)
                break
            else:
                print(invalidsms)
def MinusMode():
    while True:
        num1, num2 = RandomNum()
        correct_answer = CalculateNum(num1,'-',num2)
        try:
            user_answer = input(f'{num1} - {num2} = ')
            correct_answer, user_answer = abs(correct_answer), int(user_answer)
            if user_answer == correct_answer:
                print("It's true")
                UserScore(scorepoint = '+')
            elif user_answer != correct_answer:
                print(f"Not True, The Correct Answer is {correct_answer}")
                UserScore(scorepoint = '-')
            else:
                print(invalidsms)
        except ValueError:
            if user_answer in exitstr:
                print(byebyesms)
                break
            else:
                print(invalidsms)   
def TimesMode():
    while True:
        num1, num2 = RandomNum()
        correct_answer = CalculateNum(num1,'*',num2)
        try:
            user_answer = input(f'{num1} * {num2} = ')
            correct_answer, user_answer = abs(correct_answer), int(user_answer)
            if user_answer == correct_answer:
                print("It's true")
                UserScore(scorepoint = '+')
            elif user_answer != correct_answer:
                print(f"Not True, The Correct Answer is {correct_answer}")
                UserScore(scorepoint = '-')
            else:
                print(invalidsms)
        except ValueError:
            if user_answer in exitstr:
                print(byebyesms)
                break
            else:
                print(invalidsms)
def DivisionMode():
    while True:
        num1, num2 = RandomNum()
        correct_answer = CalculateNum(num1,'/',num2)
        try:
            user_answer = input(f'{num1} / {num2} = ')
            user_answer = float(user_answer)
            if user_answer == correct_answer:
                print("It's true")
                UserScore(scorepoint = '+')
            elif user_answer != correct_answer:
                print(f"Not True, The Correct Answer is {correct_answer}")
                UserScore(scorepoint = '-')
            else:
                print(invalidsms)
        except ValueError:
            if user_answer in exitstr:
                print(byebyesms)
                break
            else:
                print(invalidsms)
def EasyMode():
    while True:
        game_mode = 'easy'
        oprator, correct_answer, num1, num2 = CalculateRan(game_mode)
        try:
            user_answer = input(f'{num1} {oprator} {num2} = ')
            correct_answer, user_answer = abs(correct_answer), int(user_answer)
            if user_answer == correct_answer:
                print("It's true")
                UserScore(scorepoint = '+')
            elif user_answer != correct_answer:
                print(f"Not True, The Correct Answer is {correct_answer}")
                UserScore(scorepoint = '-')
            else:
                print(invalidsms)
        except ValueError:
            if user_answer in exitstr:
                print(byebyesms)
                break
            else:
                print(invalidsms)
def MediumMode():
    while True:
        game_mode = 'medium'
        oprator, correct_answer, num1, num2 = CalculateRan(game_mode)
        try:
            user_answer = input(f'{num1} {oprator} {num2} = ')
            correct_answer, user_answer = abs(correct_answer), int(user_answer)
            if user_answer == correct_answer:
                print("It's Correct")
                UserScore(scorepoint = '+')
            elif user_answer != correct_answer:
                print(f"Not Correct, The Correct Answer is {correct_answer}")
                UserScore(scorepoint = '-')
            else:
                print(invalidsms)
        except ValueError:
            if user_answer in exitstr:
                print(byebyesms)
                break
            else:
                print(invalidsms)
def HardMode():
    while True:
        game_mode = 'hard'
        oprator, correct_answer, num1, num2 = CalculateRan(game_mode)
        try:
            user_answer = input(f'{num1} {oprator} {num2} = ')
            correct_answer, user_answer = abs(correct_answer), float(user_answer)
            if user_answer == correct_answer:
                print("It's Correct")
                UserScore(scorepoint = '+')
            elif user_answer != correct_answer:
                print(f"Not Correct, The Correct Answer is {correct_answer}")
                UserScore(scorepoint = '-')
            else:
                print(invalidsms)
        except ValueError:
            if user_answer in exitstr:
                print(byebyesms)
                break
            else:
                print(invalidsms)
def PracticeMode():
    # Practice Mode Validation
    plus_mode = ['1','+','plus','addition']
    minus_mode = ['2','-', 'minus', 'subtraction']
    times_mode = ['3', 'X', '*', 'times', 'multiplication']
    division_mode = ['4', '/', 'division']
    practice_mode = str(input('''
1. + Plus Addition
2. - Minus Subtraction
3. X * Times Multiplication
4. / Division
0. Exit
Enter Practice Mode: '''))
    while True:
        if practice_mode in exitstr:
            print(notselectedsms, exitsms)
            break
        elif practice_mode in plus_mode:
            print(selectsms, plussms)
            PluseMode()
            break
        elif practice_mode in minus_mode:
            print(selectsms, minussms)
            MinusMode()
            break
        elif practice_mode in times_mode:
            print(selectsms, timessms)
            TimesMode()
            break
        elif practice_mode in division_mode:
            print(selectsms, divisionsms)
            DivisionMode()
            break
        else:
            practice_mode = str.lower(input('Invalid mode, try again: '))
def GameMode():
    # Practice Mode Validation
    easy = ['1','easy']
    medium = ['2','medium']
    hard = ['3','hard']
    game_mode = str(input('''
1. Easy   + and -
2. Medium * and + and -
3. Hard   / and * and + and -
0. Exit
Select Game mode: '''))
    while True:
        if game_mode in exitstr:
            print(notselectedsms, exitsms)
            break
        elif game_mode in easy:
            print(selectsms, easysms)
            EasyMode()
            break
        elif game_mode in medium:
            print(selectsms, mediumsms)
            MediumMode()
            break
        elif game_mode in hard:
            print(selectsms, hardsms)
            HardMode()
            break
        else:
            game_mode = str.lower(input('Invalid mode, try again: '))

def MathGame():
    # Mode Validation
    practice = ['1','one','practice']
    game = ['2','two','game']
    select_mode = str.lower(input('''
1. Practice
2. Game
0. Exit
Enter Mode: '''))
    while True:
        if select_mode in exitstr:
            print(notselectedsms, exitsms)
            break
        elif select_mode in practice:
            print(selectsms, practicesms)
            PracticeMode()
            break
        elif select_mode in game:
            print(selectsms, gamesms)
            GameMode()
            break
        else:
            select_mode = str.lower(input('Invalid mode, try again: '))

# Math Game Version 1.1
# one
UserName()