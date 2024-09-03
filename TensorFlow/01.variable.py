'''
import tensorflow as tf
#criando tensor com tf.variable

changeble_tensor = tf.Variable([10,7])  #letra maiúscula
unchangeble_tensor = tf.constant([10,7])
changeble_tensor, unchangeble_tensor
#muda elementos
changeble_tensor[0].assign(7) #unchangeble não muda
changeble_tensor

#random tensores, o tensorflow vai criar tensores para vc, caso precise fazer use constantes
random_1 = tf.radsom.Generator.from_seed(47)  #defina o seed para reprodutividade


'''