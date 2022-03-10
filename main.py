'''Escrever um programa em linguagem Python que lê um valor i inteiro e positivo e 3 valores a,b,c. Se o valor de i é par então calcular e imprimir na tela a média aritmética de A, B e C. Caso contrário, se i>0, então calcular e imprimir na tela a média aritmética e ponderada de A, B e C. Os pesos dos valores são respectivamente 2, 3 e 4.'''

i = int(input('Digite um valor inteiro e positivo: \n'))
if i<=0:
  print('Não é possível prosseguir. \nDigite um valor a partir de 1.')
elif i % 2 == 0 and i<=10 and i>0:
  a = float(input('Digite o valor de A: \n'))
  b = float(input('Digite o valor de B: \n'))
  c = float(input('Digite o valor de C: \n'))
  media1 = (a+b+c)/3
  print ('A média dos valores digitados é igual a: {:.2}'.format(media1))
elif i > 10 :
  a = float(input('Digite o valor de A: \n'))
  b = float(input('Digite o valor de B: \n'))
  c = float(input('Digite o valor de C: \n'))
  media1 = (a+b+c)/3
  media2 = (a*2+b*3+c*4)/9
  print('A média aritmética dos valores de A({}),B ({}) e C ({}) é equivalente há {:.2} e a média ponderada dos mesmos é equivalente há {:.2} '.format(a, b, c, media1, media2))
else:
  print('O valor de digitado é ímpar menor que 10. Entretanto insira os valores a seguir para obter a sua média. \n')
  a = float(input('Digite o valor de A: \n'))
  b = float(input('Digite o valor de B: \n'))
  c = float(input('Digite o valor de C: \n'))
  media1 = (a+b+c)/3
  print ('A média dos valores digitados é igual a: {:.2}'.format(media1))