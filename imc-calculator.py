def resultado():
  if imc < 18.5:
    print('Resultado: MAGREZA')
  elif imc > 18.5 and imc < 24.9:
    print('Resultado: NORMAL')
  elif imc > 25.0 and imc < 29.9:
    print('Resultado: SOBREPESO')
  elif imc < 30.0 and imc < 39.9:
    print('Resultado: OBESIDADE')
  elif imc >= 40.0:
    print('Resultado: OBESIDADE GRAVE')
  else:
    print('VALOR INCORRETO!')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
print('')
print('IMC: {:.2f}'.format(imc))
print('')
resultado()
