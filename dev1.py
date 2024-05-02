def cria_mapa(n):
    mapa = []
    colunas = []
    space = ' '

    for e in range(n):
        colunas.append(space)

    for e in range(n):
        mapa.append(colunas)

    return mapa