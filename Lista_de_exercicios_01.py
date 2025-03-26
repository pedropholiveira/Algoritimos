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

# EXERCICIO11
# Levando em conta as relações entre unidaddes de temperatura mostradas nos 6 primeiros exercicios, faça
# um programa em python que converte temperaturas expressas em graus kelvin para graus rankine. Seu programa deve solicitar o valor a ser convertido k

# print("Programa para a conversão de temperatura kelvin para rankine ")

# try:
#     tempr = float(input("Insira o valor da temperatura em graus Kelvin: "))
# except ValueError:
#     print("O valor digitado deve ser um numero valido!! ")
# else:
#     print("O valor de temperatura em graus kelvin ", tempr,
#           " e seu valor equivalente em graus rankine ", tempr*9/5)


# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO12
# Levando em conta as relações entre unidades de temperatura mostradas nos 6 primeiros exercicios, faça um programa
# em python que converte temperaturas expressas em graus rankine para graus kelvin. Seu programa devesolicitar a digitação do valor a ser convertido

# print("Programa para a conversão de temperatura em graus Rankine para Kelvin ")

# try:
#     tempr = float(input("Insira o valor da temperatura em graus rankine: "))
# except ValueError:
#     print("O valor inserido deve ser numerico!!")
# else:
#     print("O valor da temperatura em graus rankine ", tempr,
#           " e seu valor equivalente em graus farenheit ", tempr-459.67)

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO13
# Lembrando que o perimetro de uma figura é a medida do controno dela, faça um programa em python que
# calcula o perimetro em contimetros de um quadrado/losango. Seu programa deve solicitar a digitação da medida em
# centimetros do lado l do quadrado/losango

# print("Programa para o calculo de perimetro de quadrados e losangos ")

# try:
#     medida_lado = float(
#         input("Insira a medida em cm do lado do quadrado/losano: "))
# except ValueError:
#     print("O valor inserio precisa ser numerico!! ")
# else:
#     print("A medida do perimetro do quadrado/losango inserido é de ",
#           medida_lado*4, " cm")


# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO14
# Lembrando que o perimetro de uma figura é a medida do contorno dela, faça um programa em python que
# calcula o perimetro em centimetros de um triangulo. seu programa deve solicitar a digitação da medida em centimetros dos lados (A,B e C)

# print("programa para calculo de perimetro de triangulos ")

# digitou_certo = False
# while digitou_certo == False:
#     try:
#         lado_A = float(input("Insira a medida do lado A em cm: "))
#     except ValueError:
#         print("O valor inserido deve ser numerico e inteiro!! ")
#     else:
#         digitou_certo = True

# digitou_certo = False
# while digitou_certo == False:
#     try:
#         lado_B = float(input("Insira a medida do lado B em cm: "))
#     except ValueError:
#         print("O valor inserido deve ser numerico e inteiro!! ")
#     else:
#         digitou_certo = True

# digitou_certo = False
# while digitou_certo == False:
#     try:
#         lado_C = float(input("Insira a medida do lado C em cm: "))
#     except ValueError:
#         print("O valor inserido deve ser numerico e inteiro!! ")
#     else:
#         digitou_certo = True

# print("O perimetro do triangulo inserido mede ", lado_A+lado_B+lado_C, " cm")


# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO15
# Lembrando que o perimetro de uma figura é a medida do contorno dela, faça um programa em python que calcula
# o perimetro em centimetros de um retangulo/paralelogramo. Seu programa deve solicitar a digitação da medida em centimetros
# lado menor (m) e do lado maior (M) do retangulo/paralelogramo.

# print("Programa para calculo de perimetro de paralelogramos ")

# try:
#     m = float(input("Insira a medida do menor lado da figura em cm: "))
# except ValueError:
#     print("O valor inserido precisa ser numerico!! ")
# else:
#     try:
#         M = float(input("Insira a medida do maior lado da figura em cm: "))
#     except ValueError:
#         print("O valor inserido precisa ser numerico!! ")
#     else:
#         print("O perimetro da figura inserida é ", m*2+M*2)

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO16
# Lembrando que o perimetro de uma figura é a medida do contorno dela, faça um programa em
# python que calcula o perimetro em centimetros de um trapézio. Seu programa deve solicitar a digitação
# da medida em centimetros do lado paralelo menor (m), do lado paralelo maior (M) e de outro lado (O) do trapézio,
# lembrando que os dois lados nao paralelos de um trapézio tem medidas iguais

# print("Programa para o calculo do perimetro de trapezios")

# try:
#     m = float(input("Insira a medida do menor lado paralelo do trapezio em cm: "))
# except:
#     print("O valor inserido precisa ser numerico!!!!!!")
# else:
#     try:
#         M = float(
#             input("Insira a medida do lado paralelo maior do trapezio em cm: "))
#     except:
#         print("O valor inserido precisa ser numerico!! ")
#     else:
#         try:
#             O = float(
#                 input("Insira a medida de um dos lados não paralelos do trapezio "))
#         except ValueError:
#             print("O valor inserido precisa ser numerico!! ")
#         else:
#             print("O perimetro do trapezio é de ", m+M+(O*2))

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO17
# Lembrando que o perimetro de uma figura é a medida do contorno dela,
# faça um programa em python que calcula o perimetro em centimetros de um poligono regular. Seu
# programa deve solicitar a digitação da quantidade de lados (Q) e a medida em centimetros de um dos lados do poligono

# print("Programa para calculo de perimetro de figura regular")

# try:
#     q = int(input("insira a quantidade de lados do poligono: "))
# except ValueError:
#     print("O numero inserido devera ser inteiro e natural")
# else:
#     try:
#         m = float(input("Insira a medida do lado em cm: "))
#     except ValueError:
#         print("O numero inserido devera ser inteiro e natural")
#     else:
#         print("O perimetro da figura mede ", q*m, " cm")


# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO18
# Lembrando que o perimetro de uma figura e a medida do contorno dela, faça um
# programa em python que calcula o perimetro em centimetros de um circulo. Seu
# programa deve solicitar a digitação da medida em centimetros do raio (R) do circulo. A relação
# entre essas grandezas é Area= 2.pi.R, sendo pi constante e aproximadamente 3,1415

# print("Programa oara calcuclo de perimetro de circunferencia ")

# try:
#     r = float(input("Insira a medida do raio da circunferencia em cm: "))
# except ValueError:
#     print("O valor precisa ser numerico!!")
# else:
#     print("O perimetro da circunferencia é de ", r*3.1415*2)

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO19
# Faça um programa em python que calcula a area em centimetros quadrados
# de um triangulo. Seu programa deve solicitar a digitação da medida emcentimetros da
# base (B) e da altura (A) do triangulo. A relação entre essas grandezas é area=(B*A)/2

# print("Programa paracalco de area de Triangulos")

# try:
#     b = float(input("Inisra a medida da base do triangulo em cm: "))
# except ValueError:
#     print("O valor deve ser numerico")
# else:
#     try:
#         a = float(input("Insira o valor daaltura do triangulo em cm: "))
#     except ValueError:
#         print("O valor deve ser numerico")
#     else:
#         print('a area do triangulo mede ', (b*a)/2)

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO20
# Faça um programa em python que calcula a area em centimetros quadrados de um quadrado. Seu programa
# deve solicitar a digitação da medida em centimetros do lado (L) do quadrado. A relação entre essas grandezas é area=L²

# print("Programa para o calculo de area de quadrados ")

# try:
#     l = float(input("Insira a medida do lado do quadrado em cm: "))
# except ValueError:
#     print("O valor deve ser numerico")
# else:
#     print('A area do quadro mede ', (l*l), " cm²")

# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO


# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO


# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO


# <--------------------------------------------------------------------------------------------------------------->

# EXERCICIO


# <--------------------------------------------------------------------------------------------------------------->
