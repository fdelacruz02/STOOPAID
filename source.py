from random import randint, choice

max_dig = int(input('enter number of digits: '))
max_num = 10**max_dig
operators = []
op_dict = {'addition':'+', 'subtraction': '-', 'multiplication': '*', 'division': '/'}
print('press [Y] for yes.')
for k in op_dict.keys():

    inp = input(f"would you like to include {k} problems? ")
    if inp.lower() == 'y':
        operators.append(op_dict[k])

def get_operands(max_num, operator):
    n1 = randint(1, max_num)
    n2 = randint(1, max_num)
    if operator == '-' and n2 > n1:
        n1, n2 = n2, n1
    elif operator == '/':
        while n1 % n2 != 0:
            n1 = randint(1, max_num)
            n2 = randint(1, max_num)
    return n1, n2


while True:
    operator = choice(operators)
    n1, n2 = get_operands(max_num, operator)
    problem = f"{n1} {operator} {n2}"
    answer = eval(problem)
    print(problem)
    user_answer = int(input('Enter answer: '))
    if answer == user_answer:
        print('\nGood job')
    else:
        count = 0
        while answer != user_answer and count != 3:
            user_answer = int(input('Enter answer: '))
            count += 1
        if count == 3:
            print("\nthe answer is ", answer)
            print("\n\n\n\n\nhere comes the next problem\n")

