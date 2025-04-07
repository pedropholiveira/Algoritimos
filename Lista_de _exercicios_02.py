# Lista de exercicios02

# Melhorias

# Exercicios de 1 a 27
# Refaça os exercicios de 1 a 27 da primeira lista de exercicios
# (exercicios de sequencia), agora validando as digitações dos usuarios.
# Para tanto, alem das peculiaridades que cada exercicio possa ter, lembre-se
# que temperaturas não podem ser inferiores ao zero absoluto (zero graus kelvin).
# Lembre-se tambem que medidas tomadas de figuras geometricas jamais poderão ser negativas e nem zero.

# EXERCICIO28

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO31
# Faça um programa em python solicite a digitação de dois valores quaisquer, informando-os em seguida, em ordem crescente.
print("BE VINDO A CALCULADORA DE NUMEROS CRESCENTES")
digitou_correto = False
while digitou_correto == False:
    while digitou_correto == False:
        try:
            numero1 = float(input("insira o valor do primeiro numero: "))
        except ValueError:
            print("O valor deve ser numerico!!")
        else:
            digitou_correto = True

    digitou_correto = False
    while digitou_correto == False:
        try:
            numero2 = float(input("insira o valor do segundo numero: "))
        except ValueError:
            print("O valor digitado deve ser numerico!!")
        else:
            digitou_correto = True
if numero1 > numero2:
    print(numero1, ",", numero2)
elif (numero1 < numero2):
    print(numero2, ",", numero1)
else:
    print("Os valores digitados são iguais: ")
# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO


# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO


# <--------------------------------------------------------------------------------------------------------------->
