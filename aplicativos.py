import adivinhacao
import forca
import imc


def escolhe_jogo():
    print("**********************************************************")
    print("********** APLICATIVOS DESENVOLVIDOS COM PYTHON **********")
    print("**********************************************************")

    print(" (1) Jogo da Forca (2) Jogo da Adivinhação (3) Calculadora IMC")

    jogo = int(input("Escolha o Aplicativo: "))


    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 3):
        print("Calculadora IMC")
        imc.calcula_imc()

if(__name__ == "__main__"):
    escolhe_jogo()