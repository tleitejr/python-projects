from math import sqrt
def funcao01():
  print('')
  print('(1) Calcular a medida da hipotenusa.')
  print('')
  print('Fórmula: a² = b² + c²')
  print('')
  b = int(input('b = '))
  c = int(input('c = '))
  print('')
  print('a² = {}² + {}²'.format(b,c))
  b2 = b * b
  c2 = c * c
  print('a² = {} + {}'.format(b2,c2))
  p = b2 + c2
  if p < 0:
    print('a  = {}'.format(p))
  else:
    print('a² = {}'.format(p))
    print('a  = √{}'.format(p))
    r = sqrt(p)
    print('a  = {:.2f}'.format(r))
  print('')
  esc = input('Deseja calcular novamente? (s/n): ')
  print('------------------------------------')
  if esc == 's':
    funcao01()
  else:
    telainicial()
    
def funcao02():
  print('')
  print('(2) Calcular a medida de um dos catetos.')
  print('')
  print('Fórmula: b² = a² - c²')
  print('')
  a = float(input('a = '))
  c = float(input('c = '))
  print('')
  print('b² = {}² - {}²'.format(a,c))
  a2 = a * a
  c2 = c * c
  print('b² = {} - {}'.format(a2,c2))
  p = a2 - c2
  if p < 0:
    print('b  = {}'.format(p))
  else:
    print('b² = {}'.format(p))
    print('b  = √{}'.format(p))
    r = sqrt(p)
    print('b  = {}'.format(r))
  print('')
  esc = input('Deseja calcular novamente? (s/n): ')
  print('------------------------------------')
  if esc == 's':
    funcao02()
  else:
    telainicial()

def funcao03():
  print('')
  print('(3) Comprovar se um triângulo é retângulo.')
  print('')
  print('Fórmula: a² = b² + c²')
  print('')
  a = int(input('a = '))
  b = int(input('b = '))
  c = int(input('c = '))
  print('')
  print('{}² = {}² + {}²'.format(a,b,c))
  a2 = a * a
  b2 = b * b
  c2 = c * c
  print('{} = {} + {}'.format(a2,b2,c2))
  p = b2 + c2
  print('{} = {}'.format(a2,p))
  if a2 == p:
    print('')
    print('R: O triângulo é reto, pois são resultados iguais "{} = {}".'.format(a2,p))
    print('')
  if a2 < p:
    print('')
    print('R: O triângulo é agudo, pois {} é menor que {}.'.format(a2,p))
    print('')
  if a2 > p:
    print('')
    print('R: O triângulo é obtuso, pois {} é maior que {}.'.format(a2,p))
    print('')
  else:
    print('')
  esc = input('Deseja calcular novamente? (s/n): ')
  print('------------------------------------')
  if esc == 's':
    funcao03()
  else:
    telainicial()

def telainicial():
  while True:
    print('O que você deseja fazer?')
    print('')
    print('(1) Calcular a medida da hipotenusa.')
    print('(2) Calcular a medida de um dos catetos.')
    print('(3) Descobrir o ângulo do triângulo.')
    print('(4) Sair.')
    print('')
    escolha = int(input('>>> '))
    match escolha:
      case 1:
        funcao01()
      case 2:
        funcao02()
      case 3:
        funcao03()
      case 4:
        print('Bye :)')
        print('')
        print('  "Com organização e tempo, acha-se o segredo de fazer tudo e bem feito." - Pitágoras de Samos (497 a.C - 582 a.C)')
        print('')
        print('GitHub: github.com/tleitejr')
        break

print('Bem-vindo a calculadora de Teorema de Pitágoras!')
print('')
telainicial()