'''
lists and tuples
'''
#listas: coleções de dados
familia= ["Eu", "Matheus", "mãe", "pai", "outros"]
familia[1] = "metheus"
print(familia)
#print(familia[1])
#print(familia[1:]) #do 1 em diante
#print(familia[-1])
#print(familia[1:4]) #todo o intervalo menos o último
familia.extend(["sem dog", "Sem cat"])  #une com uma lista (1 ou mais itens). pode colocar o nome de outra lista dentro
familia.append("no excuses") #une com um item
print(familia)
familia.insert(1,"Eu denovo")
familia.pop()
familia.remove("sem dog")
print(familia)
#familia.clear()
#print(familia)
#print(familia.index("Eu"))
#print(familia.count("Eu"))

idades = [19, 75, 23, 49, 8]
idades.sort()
idades.reverse()
print(idades)
#familia.sort()
#print(familia) pode colocar string em ordem alfabética tbm

#familia2 = familia #Familia2 é só 1 cópia de referencia, so tá apontando para o mesmo espaço de memória
familia2 = familia.copy() #vai criar uma nova lista
print(familia2)
familia.remove("Eu denovo")
print(familia2)

#tuplas uma lista só que com elementos imutáveis, tem todas as funções da lista menos as q mudam algo

coordenadas = (-10, -5) 
print(coordenadas[1])
print(type(coordenadas))