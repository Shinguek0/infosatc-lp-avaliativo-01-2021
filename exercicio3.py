'''Um determinado prêmio de loteria saiu para um bolão de três amigos. Uma lei
garante que todo prêmio de loteria deva pagar um imposto de 7% para os
cofres estaduais. Do total descontado o imposto, os amigos irão dividir o prêmio
da seguinte maneira:
O primeiro ganhador recebera 46%;
O segundo recebera 32%;
O terceiro recebera o restante;
Faça um programa que leia o valor total do prêmio, calcule o desconto, o valor
que cada um tem direito e imprima o total do prêmio, o premio descontado o
imposto e a quantia recebida por cada um dos ganhadores'''

premio = float(input("Digite o valor do premio: "))
premioDescontado = premio - (premio/100)*7

g1 = premioDescontado - (premioDescontado/100)*54
g2 = premioDescontado - (premioDescontado/100)*68
g3 = premioDescontado - (g1 +g2)
print("Valor total do premio:", premio)
print("Valor do premio com desconto do imposto:",premioDescontado)
print("Primeiro ganhador fica com R${:.2f} \nO segundo fica com R${:.2f} \nE o terceiro fica com R${:.2f}".format(g1,g2,g3))