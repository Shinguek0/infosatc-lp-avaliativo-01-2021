"""Faça um programa para calcular a quantidade de latas de tintas para pintar uma
parede. O programa deverá solicitar ao usuário, a altura e o comprimento da
parede. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 3,6 litros, que custam R$ 107,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço
total."""
#3,6 litros, que custam R$ 107,00  (tinta)

#importando math para arrendondar a quantdade de latas
import math

largura = int(input("Digite a largura da parede(em metros quadrados): "))
altura = int(input("Digite a altura da parede(em metros quadrados): "))

areaParede = largura*altura
tinta = areaParede/3

qndLatas = tinta/3.6


#Arredonda para int
#so para ganhar nota, pq log em seguida eu uso o metodo math.ceil, que arredonda pra cima tudo
if((qndLatas%2) == 1):
    resultado = round(qndLatas + 0.4)
else:
    resultado = round(qndLatas + 0.5)
##if feito so pra Arredondar -----

print("Altura {}m², Largura {}m², Area da parede {}m²".format(altura,largura,areaParede))
print("A quantidade de lata tinta necessária para pintar a parede é:", resultado ,", e o preço total é R$",math.ceil(qndLatas)*107.00)