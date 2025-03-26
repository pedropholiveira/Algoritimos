# Faça um programa em python que converte temperaturas expressas em graus Farenheit para graus
# celsius. seu programa deve solicitar a digitação do valor convertido (F). A relação entre gruas
# celsius e graus farenheit é c = 5/(f-32)

print("Programa para conversão de te temperatura C° p/ F° ")

try:
    tempF = float(
        input("Insira a temperatura em Farenheit: "))
except ValueError:
    print("O VALORR DIGITADO DEVE SER UM NUMERO!!")
else:
    print("A temepratura digitada em graus Farenheit foi de ", tempF,
          " e seu valor correspondente em graus Celsius é ", (5/9*(tempF-32)))
