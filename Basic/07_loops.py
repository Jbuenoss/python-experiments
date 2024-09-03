# i = 1
# while i <= 10: 
#     print(i)
#     i += 1        #para comentar toda a parte do código: (ctrl + ;)

# palavra = "João Bueno"
# for letra in palavra:
#     print(letra)

# lista = ["João", "Bueno", "Costa"]
# for palavra in lista:
#     print(palavra)

print("0 ao 19:")
for index in range(20):     #range tem 3 parametros, 1 é obrigatório (o de parada). começa do 0 por padrão
    print(index)
print("fim do 0 ao 19:")

# for index in range(1, 20, 2):       #inicio, final, tamanho do pulo
#     print(index)

# for index in range(len(lista)):
#     print(f"{lista[index]}, {index}")

#lista de lista = matriz
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [10, 11, 12],
]
for linha in matrix:
    print(linha)
    for coluna in linha:
        print(coluna)