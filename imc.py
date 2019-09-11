
def calcula_imc():
    print("******************************************")
    print("************CALCULADORA DE IMC************")
    print("******************************************")

    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))
    classificacao = "normal"
    imc = peso / (altura * altura)
    imc = round(imc, 2)

    if imc < 18.5:
        classificacao = "MAGREZA"
    elif imc > 18.5 and imc < 24.9:
        classificacao = "NORMAL"
    elif imc > 24.9 and imc < 29.9:
        classificacao = "SOBREPESO GRAU I"
    elif imc > 29.9 and imc < 39.9:
        classificacao = "OBESIDADE GRAU II"
    elif imc > 39.9:
        classificacao = "OBESIDADE GRAVE GRAU III"

    print("O seu IMC é {} e sua classificação conforme a OMS é {}".format(imc,classificacao))

if(__name__ == "__main__" ):
    calcula_imc()