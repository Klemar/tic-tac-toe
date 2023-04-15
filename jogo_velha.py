import os

# Define o tabuleiro inicial
tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Define as funções

def desenha_tabuleiro():
    os.system("cls")
    print("\n")
    print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2] + " ")
    print("---|---|---")
    print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5] + " ")
    print("---|---|---")
    print(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8] + " ")
    print("\n")

def jogada(jogador):
    posicao = int(input("Digite a posição para jogar (1-9): ")) - 1
    if tabuleiro[posicao] == " ":
        tabuleiro[posicao] = jogador
    else:
        print("Posição já jogada!")
        jogada(jogador)

def verifica_ganhador():
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] and tabuleiro[i+1] == tabuleiro[i+2] and tabuleiro[i] != " ":
            return tabuleiro[i]
    for i in range(0, 3):
        if tabuleiro[i] == tabuleiro[i+3] and tabuleiro[i+3] == tabuleiro[i+6] and tabuleiro[i] != " ":
            return tabuleiro[i]
    if tabuleiro[0] == tabuleiro[4] and tabuleiro[4] == tabuleiro[8] and tabuleiro[0] != " ":
        return tabuleiro[0]
    if tabuleiro[2] == tabuleiro[4] and tabuleiro[4] == tabuleiro[6] and tabuleiro[2] != " ":
        return tabuleiro[2]
    if " " not in tabuleiro:
        return "Empate"
    return None

# Define a variável do jogador atual
jogador_atual = "X"

# Inicia o jogo
while True:
    desenha_tabuleiro()
    jogada(jogador_atual)
    ganhador = verifica_ganhador()
    if ganhador is not None:
        desenha_tabuleiro()
        if ganhador == "Empate":
            print("Empate!")
        else:
            print(ganhador + " ganhou!")
        break
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"