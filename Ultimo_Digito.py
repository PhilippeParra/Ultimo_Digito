"""Programa para identificar de
un numero dado si su ultimo digito
es par"""

print("-----------------------------------------------")
print("---------¿Ultimo Digito Par?-------------")
print("-----------------------------------------------")

#input
X = int(input("digite el valor de X: "))

#processing

ultimo_digito = X % 10

Z = ultimo_digito % 2

if Z == 0:
    msj = "El ultimo digito es par"


#output

print(msj)