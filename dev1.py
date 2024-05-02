def cria_mapa(n):
    mapa = []
    colunas = []
    space = ' '

    for e in range(n):
        colunas.append(space)

    for e in range(n):
        mapa.append(colunas)

    return mapa


def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    tamanho_mapa = len(mapa)   

    if linha < 0 or coluna < 0 or linha >= tamanho_mapa or coluna >= tamanho_mapa:
        return False
    
    if orientacao == 'v':
        for i in range(blocos):
            if linha + i >= tamanho_mapa or mapa[linha + i][coluna] != ' ':
                return False

    elif orientacao == 'h':
        for i in range(blocos):
            if coluna + i >= tamanho_mapa or mapa[linha][coluna + i] != ' ':
                return False
                
    else:
        return False
    
    return True