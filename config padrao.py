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

CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}