'''
import numpy as np
import pandas as pd
#Digite pd. e depois espere para ver todas as funções
#? e ?? entra mais a fundo na documentação

list_1 = ["a", "b", "d", "d"]
labels_1 = [1, 2, 4, 5]
ser_1 = pd.Series(data=list_1, index=labels_1)  #series: tipo de dado unidimensional
ser_1

list_2 = np.array([1, 2, 3, 4])
ser_2 = pd.Series(list_2) #Cuidado letra maiúscula!
ser_2   

dict_1 = {'1º' : "João", '2º':"Bueno", '3°':3}
ser_3 = pd.Series(dict_1)
ser_3 #series suporta diferente tipos de dados
ser_3['1º']
ser_2.dtype

ser_1 + ser_1
ser_2 / ser_2

np.exp(ser_2)

#dicionário é com chaves {}
ser_4 = pd.Series({1:2, 2:3, 3:4}, name="nothing")
ser_4.name
'''