#---primeira questão---#
def múltiplo(a, b):
    return a % b == 0

print(f"múltiplo(8,4) {múltiplo(8,4)}")
print(f"múltiplo(7,3) {múltiplo(7,3)}")
print(f"múltiplo(5,5) {múltiplo(5,5)}")

#---segunda questão---#
arq = float(input('Qual o tamanho do arquivo(MB) ? '))
val = float(input('Qual a velocidade do link(Mbps) ?'))
print(f'O tempo para download do arquivo é de: {((arq/val) * 60):0.0f} minutos')

#---terceira questão---#
a = 80000
b = 200000
ano = 0

while a <= b:
	a += a * 0.03
	b += b * 0.015
	ano += 1
print (f'A quantidade de anos para que a população A iguale a B ou ultrapasse é de {ano}')

#---quarta questão---#
res1 = int(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res2 = int(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res3 = int(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res4 = int(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res5 = int(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
soma_respostas = res1 + res2 + res3 + res4 + res5
if (soma_respostas < 2):
    print("\nInocente")
elif (soma_respostas == 2):
    print("\nSuspeita")
elif (3 <= soma_respostas <= 4):
    print("\nCúmplice")
elif (soma_respostas == 5):
    print("\nAssassino")
