# EXERCICIO 1
# Faça um programa em python que converte temperaturas expressas em graus Farenheit para graus
# celsius. seu programa deve solicitar a digitação do valor convertido (F). A relação entre gruas
# celsius e graus farenheit é c = 5/(f-32)

# print("Programa para conversão de te temperatura F° p/ C°")

# try:
#     tempF = float(
#         input("Insira a temperatura em Farenheit: "))
# except ValueError:
#     print("O VALORR DIGITADO DEVE SER UM NUMERO!!")
# else:
#     print("A temepratura digitada em graus Farenheit foi de ", tempF,
#           " e seu valor correspondente em graus Celsius é ", (5/9*(tempF-32)))


# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO2
# Faça um programa que converte temperaturas expressas em gruas celcius para gruas farenheit.Seu
# programa deve solicitar a digitação do valor a ser convertido (c). A relação entre graus celcius e graus farenheit é c=5/9(f-32)

# print("Programa para conversão de temperatura F° p/ C°")

# try:
#     tempc = float(input("Insira a temperatura em Celsius: "))
# except ValueError:
#     print("O valor inserido deve ser um numero!!")
# else:
#     print("A tempertura inserida em graus celsius foi de ", tempc,
#           " e seu valor correspondente em gruas farenheit é ", (tempc*(9/5))+32)

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO3
# Faça um programa em python que converte temperaturas expressas em graus celcius para graus kelvin. Seu programa deve solicitar a digitação
# do valor a ser convertido (c). A relação entre graus celsius e grau kelvin é c= k-273,15

# print("Programa para a conversão de temperaturas C° p/ K° ")

# try:
#     tempc = float(input("Insira o valor da temperatura em graus Celsius: "))
# except ValueError:
#     print('O valor inserido deve ser um numero!! ')
# else:
#     print("A temperatura inserida em gruas celsius é ", tempc,
#           " e seu valor correspondente em graus kelvin é ", (tempc+273.15))

# <--------------------------------------------------------------------------------------------------------------->


# EXERCICIO4
# Faça um programa em python que converte temperaturas expressas em graus kelvin para graus celsius. Seu programa deve solicitar a digitação do valor a ser
# convertido (k). A relação entre graus celsius e graus kelvin é c=k-273,15

# print("Programa para a conversão de k° para c°")

# try:
#     tempk = float(input("Insira o valor da temperatura em graus Kelvin: "))
# except ValueError:
#     print("O valor inserido deve ser um um numero! ")
# else:
#     print("A temperatura inserida em graus kelvin foi de ", tempk,
#           "e seu valor correspondente em graus celsius é de ", tempk-273.15)

# <--------------------------------------------------------------------------------------------------------------->
# EXERCICIO5
# Faça um programa em pythin que converte temeperaturas expressas em graus celsius para graus rankine. seu programa
# deve solicitar a digitação do valor a ser convertido (C). A relação entre graus celsius e graus rankine é c=(r/1.8)-491,97

# print("Programa para conversão de graus celsius rankine para graus celsius")

# try:
#     tempc = float(input("Insira o valor da temperatura em graus Rankine: "))
# except ValueError:
#     print("O valor inserido deve ser um numero!!!")
# else:
#     print('O valor inserido em graus Rankine foi de ', tempc,
#           " e seu valor correspondente em graus celcius é ", (tempc-491.67)*5/9)

# <--------------------------------------------------------------------------------------------------------------->
# EXERCICIO6
# Faça um programa que converte temperaturas expressas em graus rankine para graus celsius.Seu programa deve
# solicitar a digitação do valor a ser convertido (c). A relação entre graus rankine é c=(r/1.8)-491.67

# print("Programa para conversão de graus Rankine para graus Celsius")

# try:
#     tempr = float(input("Insira o valor da temperatura em grua rankine: "))
# except ValueError:
#     print("O valor inserido deve ser um nuemro!!")
# else:
#     print("O valor digitado em graus rankine foi de ", tempr,
#           " e seu valor correspondente em graus celsius é de ", (tempr-491.67)*5/9)

# <--------------------------------------------------------------------------------------------------------------->
# EXERCICIO7
# Levando em conta as relações entre unidade de temperatura mostradas nos 6 primeiros exercicos. Faça um progrma em python
# que converte temperaturas expressas em graus kelvin para graus farenheit. Seu programa deve solicitar a digitação do valor a ser convertido (k).

# print("Programa para a conversão de graus kelvin para graus farenheit")

# try:
#     tempk = float(input("Insira o valor da temperatura em graus Kelvin: "))
# except ValueError:
#     print("O valor inserido deve ser um numero!!")
# else:
#     print("O valor da temperatura em graus Kelvin ", tempk,
#           " e seu valor correspondente em graus farenheit é de ", (tempk - 273.15)*9/5+32)

# <--------------------------------------------------------------------------------------------------------------->
# EXERCICIO8
# Levando em conta as unidades de temperatura mostradas nos 6 primeiros exercicios, faça um programa em python que converte
# temperaturas expressas em graus farenheit para graus kelvin. seu programa deve solicitar a digitação do valor a ser convertido (f)

# print("Programa de conversão de graus farenheit para kelvin ")

# try:
#     tempf = float(input("Insira o valor da temperatura em gruas Farenheit: "))
# except ValueError:
#     print("O valor digitado deve ser um numero!!")
# else:
#     print("O valor de temperatura em graus farenheit ", tempf,
#           " e seu valor coreespondente em graus kelvin é de ", (tempf-32)*5/9+273.15)

# <--------------------------------------------------------------------------------------------------------------->

# # EXERCICIO9
# Levando em conta as relações entre unidades de temperatura mostrada nos 6 primeiros exercicios, faça um programa em python
# que converte temperaturas expressas em graus farenheit para graus rankine. Seu programa deve solicitar a digitação do valor a ser convertido(f).

# print((" Programa para a conversão de graus Farenheit para graus Rankine"))

# try:
#     tempf = float(input("Insira o valor de temperatura em graus Farenheit: "))
# except ValueError:
#     print("O valor digitado ve ser numerico!!")
# else:
#     print("O valor de temperatura em graus Farenheit ", tempf,
#           " e seu valor correspondente em graus Rankine é de ", tempf+459.67)

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO10
# Levando em conta as relações entre unidades de temperatura mostradas nos 6 primeiros exercicios,faça um
# programa em python que converte temperaturas expressas em graus rankine para graus farenheit. Seu programa
# deve solicitar a digitação do valor a ser convertido (r)

# print("Programa para a conversão de graus Rankine para graus Farenheit! ")

# try:
#     tempr = float(input("Insira o valor da temperatura em graus Rankine: "))
# except ValueError:
#     print("O valor inserido deve ser numerico!! ")
# else:
#     print("O valor de temperatura em graus rankine ", tempr,
#           " e seu valor correspondente em graus farenheit é de ", tempr-459.67)

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO


# <--------------------------------------------------------------------------------------------------------------->
