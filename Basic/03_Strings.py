exemplo = "strinG tESte"
print(exemplo.upper())
print(exemplo.lower())
print(exemplo.capitalize())     #primeira letra maiúscula resto minúscula
exemplo = exemplo.capitalize()
print(exemplo.islower())
print(exemplo.isupper())

exemplo2 = "  Só teste denovo "
print(exemplo2)
exemplo2 = exemplo2.strip() #remove espaços iniciais
print(exemplo2)
print(exemplo2.replace(" ", "_", 2))

print("___________parte_2_______________")
tam = len(exemplo)
print(tam)
print(exemplo[2])
print(exemplo[8:11])
print(exemplo[-4:-1]) #indo de trás para frente os indices começam do -1

x = "teste" in exemplo
print(x)
print(exemplo.index("teste"))

print("___________Texto_com_multiplas_linhas_______________")
multi = """Linha 1
linha 2
linha 3"""
print(multi)

multi = "linha 4 \nlinha 5 \nlinha \"6\" " #caractere de escape para usar aspas no meio da string \"
print(multi)
