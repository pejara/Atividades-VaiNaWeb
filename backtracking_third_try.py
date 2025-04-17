def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|" + "|".join(linha) + "|")
    print("\n")

def movimento_valido(tabuleiro, linha, coluna):
    if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
        return tabuleiro[linha][coluna] == ' '
    return False

def chegou_destino(linha, coluna):
    return linha == 0 and coluna == 3

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade=0):
    melhor_profundidade = float('inf')
    melhor_linha, melhor_coluna = linha_atual, coluna_atual
    mostrar_tabuleiro(tabuleiro)
    
    #direita, esquerda, cima, baixo
    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    for dl, dc in direcoes:
        nova_linha = linha_atual + dl
        nova_coluna = coluna_atual + dc
        
        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            if chegou_destino(nova_linha, nova_coluna):
                print("No destino")
                return (nova_linha, nova_coluna, profundidade + 1)
            
            tabuleiro[nova_linha][nova_coluna] = '*'
            #mostrar_tabuleiro(tabuleiro)
            l, c, p = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1)
            print("Desmarcando...")
            tabuleiro[nova_linha][nova_coluna] = ' '  # backtrack
            mostrar_tabuleiro(tabuleiro)
            
            if p < melhor_profundidade:
                melhor_linha, melhor_coluna, melhor_profundidade = l, c, p
                print("Profundidade dessa tentativa: ", p)
                #print(f"Melhor resultado: linha: {melhor_linha}, coluna: {coluna_atual}, profundidade: {melhor_profundidade}")
    
    return (melhor_linha, melhor_coluna, melhor_profundidade)

def main():
    tabuleiro = [
        ['X', ' ', ' ', ' '],
        [' ', ' ', 'X', ' '],
        [' ', ' ', 'X', ' '],
        [' ', ' ', 'X', ' ']
    ]
    
    # Posição inicial
    linha_atual, coluna_atual = 3, 0
    tabuleiro[linha_atual][coluna_atual] = '*'
    
    print("Nosso tabuleiro:")
    mostrar_tabuleiro(tabuleiro)
    
    while True:
        nova_linha, nova_coluna, profundidade = proximo_movimento(tabuleiro, linha_atual, coluna_atual)
        
        if profundidade == float('inf'):
            print("Não foi possível encontrar um caminho para o destino!")
            break
        
        # Atualiza a posição atual
        tabuleiro[linha_atual][coluna_atual] = ' '
        linha_atual, coluna_atual = nova_linha, nova_coluna
        tabuleiro[linha_atual][coluna_atual] = '*'
        
        if chegou_destino(linha_atual, coluna_atual):
            print("Parabéns! Você chegou ao destino!")
            print(linha_atual,coluna_atual,profundidade)
            break

if __name__ == "__main__":
    main()

#Eu usei IA para me explicar algumas partes, e todos esses prints é para mim entender a lógica...
#Especialmente a lógica da recursão e do próximo movimento