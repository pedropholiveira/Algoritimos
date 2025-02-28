print("Programa para calculo de area de triangulo! ")

try:
    base = float(
        input("insira a medida do primeiro lado do triangulo em cm: "))
except ValueError:
    print("O VALORR DIGITADO DEVE SER UM NUMERO!!")
else:
    if base < 0:
        print("o valor inserido deve ser um numero positivo inteiro: ")
    else:
        try:
            altura = float(
                input("insira a medida do segundo lado do triangulo em cm: "))
        except ValueError:
            print("O VALORR DIGITADO DEVE SER UM NUMERO!!")
        else:
            if altura < 0:
                print("o valor inserido deve ser um numero positivo: ")
            else:
                print("A area do triangulo mede ", (base*altura)/2, " cm²")
