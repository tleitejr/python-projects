print('')
print('Olá :)')
print('Antes de começar, crie uma conta.')
nome = input('Nome: ')
correio_eletronico = input('Email: ')
senha = input('Senha: ')
print('Ok.')
print('=================================')
print('Bem-vindo(a)!')
while True:
    email = input('Email: ')
    password = input('Senha: ')
    if email == correio_eletronico and password == senha:
        print('Olá {}.'.format(nome))
        break
    else:
        print('Tente novamente \(°_°)/')
