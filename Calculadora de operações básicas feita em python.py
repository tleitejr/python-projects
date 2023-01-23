print('================================================')
print('CALCULADORA DE OPERAÇÕES BÁSICAS FEITA EM PYTHON')
print('================================================')
while True:
    print('')
    n1 = int(input('Digite um número: '))
    print('')
    ob = input('Escolha uma operação:\n Adição + \n Subtração - \n Multiplicação * \n Divisão / \n OB: ')
    print('')
    n2 = int(input('Digite o segundo número: '))
    print('')
    r = int(n1 + n2)
    if ob == '+':
        r = n1 + n2
        print('')
        print('Resultado: {}'.format(r))
        print('')
    elif ob == '-':
        r = n1 - n2
        print('')
        print('Resultado: {}'.format(r))
        print('')
    elif ob == '*':
        r = n1 * n2
        print('')
        print('Resultado: {}'.format(r))
        print('')
    elif ob == '/':
        r = n1 / n2
        print('')
        print('Resultado: {}'.format(r))
        print('')
