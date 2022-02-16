#--primeira questão--#

nota = int(input('Informe uma nota entre 0 e 10: '))
if nota <= 10:
    print(f'Muito bem! A nota informada foi {nota}')
else:
    print('Valor inválido! Informe entre 0 e 10!')

#--segunda questão--#

soma = 0
x = 0
while (x <= 4):
    num = int(input('Informe um número: '))
    x += 1 
    soma += num

print(f'A soma dos números é {soma} e a média é {soma//5}')

#--terceira questão--#

num = int(input('Tabuada do numero: '))

for n in range (11):
    print(f'{num} x {n} = {num*n}')

#--quarta questão--#

num1 = int(input('Informe um número: '))
num2 = int(input('Informe um número: '))

for n in range (num1 + 1, num2):
    print(f'{n}')

#--quinta questão--#

n1 = float(input('Informe sua 1ª nota: '))
n2 = float(input('Informe sua 2ª nota: '))
media = (n1 + n2) / 2

if (media > 9.0) and (media <= 10.0):
    print(f'Sua média foi: {media} e seu conceito A')
elif (media > 7.5) and (media <= 9.0):
    print(f'Sua média foi: {media} e seu conceito B')
elif (media > 6.0) and (media <= 7.5):
    print(f'Sua média foi: {media} e seu conceito C')
elif (media > 4.0) and (media <= 6.0):
    print(f'Sua média foi: {media} e seu conceito D')
elif (media < 4.0) and (media <= 0.0):
    print(f'Sua média foi: {media} e seu conceito E')

#--sexta questão--#
L = []
nomes = ''
x = 0

while x < 5:
    nomes = input('Digite um nome: ')
    x += 1
    if len(nomes) < 5:
        L.append(nomes)

print(f'os nomes menores que 5 caracteres:{L}')

#--sétima questão--#
vetor = []
par = []
impar = []

for numero in range(0, 20):
    vetor.append(int(input("Digite um número: ")))

for numero in range(0, 20):
    if vetor[numero] % 2 == 0:
        par.append(vetor[numero])
    else:
        impar.append(vetor[numero])

print("Vetor com 20 elementos: " + str(vetor))
print("Vetor com elementos pares: " + str(par))
print("Vetor com elementos ímpares: " + str(impar))