num_cases = int(input())
numerator = 0
denominator = 0
operators = '+-*/'


def simplifier(up, down):
    num = up
    den = down
    i = 10

    while i > 1:
        if num % i == 0 and den % i == 0:
            num /= i
            den /= i
            i = 10
        else:
            i -= 1

    if up == down:
        print(f'{up}/{down} = 1/1')
    else:
        print(f'{up}/{down} = {num:.0f}/{den:.0f}')


for i in range(0, num_cases):
    operation = input().split(' ')

    for j in range(0, len(operation)):
        if operation[j] not in operators:
            operation[j] = int(operation[j])

    if operation[3] == '+':
        numerator = (operation[0] * operation[6] + operation[4] * operation[2])
        denomimator = (operation[2] * operation[6])

    elif operation[3] == '-':
        numerator = (operation[0] * operation[6] - operation[4] * operation[2])
        denomimator = (operation[2] * operation[6])

    elif operation[3] == '*':
        numerator = (operation[0] * operation[4])
        denomimator = (operation[2] * operation[6])

    else:
        numerator = (operation[0] * operation[6])
        denomimator = (operation[4] * operation[2])

    simplifier(numerator, denomimator)
