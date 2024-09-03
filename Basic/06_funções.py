def sanduiche(nome):
    print(f"sanduiche {nome}")
def refrigerante(tipo, tamanho):
    print(f"Refrigerante tipo {tipo} {tamanho}")
def combo(nome, tipo, tamanho):
    sanduiche(nome)
    refrigerante(tipo, tamanho)
combo("João", "Coca", "Média")      #No python tudo é baseado na indentação

print("\n")

def maior_numero(lista_num):
    lista_num.sort()
    return lista_num[len(lista_num) - 1]

print(maior_numero([-1,0,55,22,567,0,4,-1222])) #Quando é para usar lista mas tá jogando direto os elementos tem q colocar entre colchetes

lista = [-2, -40, 43, 88, 9, 0]
print(maior_numero(lista))