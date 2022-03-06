def replace(x):
    import re
    lista=[]
    for i in x:
        lista.append(re.sub(" mil", "", i))
    return lista


def replace_1(x):
    import re
    lista_2=[]
    for i in x:
        lista_2.append(re.sub(",", ".", i))
    return lista_2

