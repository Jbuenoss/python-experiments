#set
#adicionar/ remover valores mas não pode modifica-los
#não pode elementos repetidos
#é desodernado, nunca vai saber a ordem que vai vir, 
#portanto não tem indice, não consegue pegar uma fruta só

frutas = {'banana', 'maca', 'beterraba', 'coringa'}
frutas.add('banana')
frutas.remove('maca')
frutas.pop()

num = {1, 11, 5, 9}
val = {True, False, True}
set1 = {'joao', 34, True} #tbm pode diferentes tipos de dados

print(frutas)
print(num)
print(set1)

