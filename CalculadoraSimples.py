while True:
    num_1 = input('Digite um número: \n')
    num_2 = input('Digite outro número: \n')
    operador = input('Digite um operador: \n')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print(f'{num_1} ou {num_2} não são válidos. Você precisa digitar um número inteiro.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print(f'Operador {operador} inválido, digite outro operador (+, -, /, * )')

    question_continue = input('Deseja continuar? \n')
    question_continue = question_continue.lower()
    if question_continue == 'y':
        continue
    else:
        break
