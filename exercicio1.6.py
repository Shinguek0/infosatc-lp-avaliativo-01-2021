#Leia uma temperatura em Cº e apresente ela em F
#formula  f = c*(9.0/5.0) + 32.0
c = float(input("Digite a temperatura em graus Celsius: "))
f = c*(9.0/5.0) + 32.0
print("Valor em Fahrenheit: %.2f"%f,"º")