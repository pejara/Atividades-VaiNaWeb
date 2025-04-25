#criar tabuleiro vazio com 9 posições
tabuleiro = [" " for _ in range(9)]

def exibir_tabuleiro():
    for i in range(0, 9, 3):
        print(f" {tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]} ")
        if i < 6:
            print("-----------")
        #imprimir linhas do tabuleiro no formato 3x3

def verificar_vencedor(tabuleiro, jogador):
    # Linhas
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] == jogador:
            return True
    # Colunas
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] == jogador:
            return True
    # Diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == jogador:
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == jogador:
        return True
    return False

def verificar_empate(tabuleiro):
    return " " not in tabuleiro

def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vencedor(tabuleiro, 'X'):
        return -10 + profundidade
    if verificar_vencedor(tabuleiro, 'O'):
        return 10 - profundidade
    if verificar_empate(tabuleiro):
        return 0

    #teste das jogadas
    if maximizando == True:
        melhor_valor = float("-inf") #menor valor, infinito negativo
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = "O"
                valor = minimax(tabuleiro, profundidade + 1, False)
                #recursão mas ele pula esse if pelo valor False ali
                tabuleiro[i] = ' '
                melhor_valor = max(melhor_valor,valor)
        return melhor_valor
    else:
        melhor_valor = float("inf") #maior valor possível
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = "X"
                valor = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = ' '
                melhor_valor = min(melhor_valor,valor)
        return melhor_valor

def melhor_jogada(tabuleiro):
    melhor_valor = -float("inf") #equivalente da 59
    melhor_posicao = -1

    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'O'
            valor = minimax(tabuleiro, 0, False)
            tabuleiro[i] = ' '

            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i
    return melhor_posicao

def jogar_jogo():
    while True:
        exibir_tabuleiro()

        #Turno do jogador X
        while True:
            try:
                jogada = int(input("Digite sua jogada (0-8): "))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == ' ':
                    break
                else:
                    print("Posição inválida ou já ocupada. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número entre 0 e 8.")

        tabuleiro[jogada] = "X"

        if verificar_vencedor(tabuleiro,'X'):
            exibir_tabuleiro()
            print("Você venceu...o que significa que tem algo de errado.")

        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Empate")
            break
        
        #computer turn
        print("GO FOURTH MY MACHINE")
        melhor_posicao = melhor_jogada(tabuleiro)
        tabuleiro[melhor_posicao] = "O"

        if verificar_vencedor(tabuleiro, 'O'):
            exibir_tabuleiro()
            print("O computador venceu, como esperado!")
            break
        
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Empate")
            break

if True: #__name__ == "__name__":
    print("Old lady game")
    print("You = X // PC = O")
    print("Posições de matriz.")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")
    print()
    jogar_jogo()

#minhas fontes principais:
#eu
#deepseek
#o pseudocódigo