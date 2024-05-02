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

import random

def aloca_navios(mapa, blocos):
    n = len(mapa)
    
    def pode_alocar(linha, coluna, orientacao, tamanho):
        if orientacao == 'h':
            return coluna + tamanho <= n and all(mapa[linha][coluna+i] == ' ' for i in range(tamanho))
        elif orientacao == 'v':
            return linha + tamanho <= n and all(mapa[linha+i][coluna] == ' ' for i in range(tamanho))
        return False

    for tamanho in blocos:
        while True:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            if pode_alocar(linha, coluna, orientacao, tamanho):
                if orientacao == 'h':
                    for i in range(tamanho):
                        mapa[linha][coluna+i] = 'N'
                elif orientacao == 'v':
                    for i in range(tamanho):
                        mapa[linha+i][coluna] = 'N'
                break
    
    return mapa

def foi_derrotado(mapa):
    lost = True
    for e in mapa:
        for i in e:
            if i == 'N':
                lost = False

    return lost