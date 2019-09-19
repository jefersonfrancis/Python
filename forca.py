import random

def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    erros = 0
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print("Parabéns, você acertou!")
    else:
        print("Que pena, você errou!")

    print("Fim de jogo!")


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    banco_de_palavras = open("banco_de_palavras.txt", "r")
    palavras = []

    for linha in banco_de_palavras:
        linha = linha.strip()
        palavras.append(linha)

    banco_de_palavras.close()
    palavra_secreta = random.choice(palavras).upper()

    return  palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


if (__name__ == "__main__"):
    jogar()