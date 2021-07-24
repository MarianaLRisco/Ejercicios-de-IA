def aplica(estado,accion):
    pos_hueco = estado.index(0)
    l = list(estado)
    if accion == "Mover hueco arriba":
        l[pos_hueco] = l[pos_hueco-3]
        l[pos_hueco-3] = 0
    return list


if __name__=='__main__':
    lista = [1,2,3,4,0,2]
    pos_hueco = lista.index(0)

    accs = list()

    if pos_hueco not in [0,1,2]:
        accs.append("Mover hueco arriba")
    print(accs)

    resultados = aplica(lista,accs)

    '''
    l= list(lista)
    for accion in accs:
        if accion == "Mover hueco arriba":
            l[pos_hueco] = l[pos_hueco-3]
            l[pos_hueco-3] = 0

    resultados = l'''

    print(resultados)


