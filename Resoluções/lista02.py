#--primeira questão--#

metros = int(input('Digite quantos metros: '))
conversão = metros * 100
print(f'Os {metros} metros convertidos em centímetros fica: {conversão} cm')

#--segunda questão--#

num = int(input('Digite um número qualquer para saber se é ímpar ou par: '))
if num % 2 == 0:
    print(f'O {num} é par!')
else:
    print(f'O {num} é ímpar!')

#--terceira questão--#

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
print(f'O número formado foi {n1}{n2}{n3}')
print(f'E o seu inverso é {n3}{n2}{n1}')

#--quarta questão--#

peso = int(input('Informe o peso do peixe: '))
excedente = peso - 50
multa = (peso - 50) * 4
if peso <= 50:
    print('Não há peso excendente, não existe multa a pagar!')
else:
    print(f'Houve peso excedente de {excedente} kilos, o valor da multa a se pagar é de R${multa}')

#--quinta questão--#
