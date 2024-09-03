'''
#deep learning: descobrir padrões em dados -- pode ser usado em tudo que pode ser transformado em números
#tensor = vetor n-dimensional, maneira numérica de representar informações
#tipos de aprendizagem, supervisionado, semi-supervisionado, não supervisionado, transferência
#dados com rótulos, alguns com rótulos, sem rótulos, usar os dados de outra deeplearning para outros dados
#vai transformar o input em tensor para a rede neural e vai receber em trocar outro tensor que você vai traduzir

import tensorflow as tf
# print(tf.__version__) #double underscore

#create tensors
 
scalar = tf.constant(7) #se nãp sabe de alguma coisa, copia e pesquisa no google que vai aparecer a documentação referente a aquilo
scalar    #é somente um número
scalar.ndim #numéros de dimensões

vector = tf.constant([10,10]) #criação de vector
vector    #é um número com direção
vector.ndim

matrix = tf.constant([[10.,7.],
                      [7.,10.],
                      [5., 2.]], dtype=tf.float16)
matrix  #2 dim de vetores de números
matrix.ndim   #continua 2, o total é igual a quantos elementos tem no shape

tensor = tf.constant([[[1,2,3],
                       [4,5,6]],
                       [[7,8,9],
                        [1,0,1]],
                      [[11,12,12],
                       [13,14,15]]])
tensor  #n-dim vetores de números
tensor.ndim
#independente de ser escalar, vector, matrix pode chamar todos eles de tensor



'''