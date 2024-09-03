from sklearn.model_selection import KFold
import numpy as np
import pandas as pd
#from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import recall_score, f1_score, precision_score

#data = load_iris()
#8x8 image of a digit.
data = load_digits()
xDF = pd.DataFrame(data.data, columns=data.feature_names)
xDF['target'] = data.target

X = xDF.drop('target', axis=1)
Y = xDF['target']

#norma = 1
normalizer = MinMaxScaler()
X_norm = normalizer.fit_transform(X)

#K fold
folds = 10
kf = KFold(n_splits=folds, shuffle=True, random_state=42)

accuracies = []
#separação treino/teste
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33,
#                                                     random_state=42)

for treino_index, teste_index in kf.split(X):
    X_treino, X_teste = X_norm[treino_index], X_norm[teste_index]
    Y_treino, Y_Teste = Y[treino_index], Y[teste_index]

    data_classifier = MLPClassifier(random_state=1, max_iter=300).fit(X_treino, Y_treino)

    Y_pred = data_classifier.predict(X_teste)

    accuracies.append(accuracy_score(Y_Teste, Y_pred))

mean_accuracie = sum(accuracies) / 10
print(f"mean accuracie = {mean_accuracie:.3f}")

matrizConfusao = confusion_matrix(Y_Teste, Y_pred)
print(matrizConfusao)
acuracia = accuracy_score(Y_Teste, Y_pred)
precisao = precision_score(Y_Teste, Y_pred, average='weighted')
sensibilidade = recall_score(Y_Teste, Y_pred, average='weighted')
f1 = f1_score(Y_Teste, Y_pred, average='weighted')

vn, fp, fn, vp = matrizConfusao.ravel()
especificidade = vn/(vn+fp)
especificidade2 = recall_score(Y_Teste, Y_pred, pos_label=0)

print('acuracia: ', acuracia)
print('precisao: ', precisao)
print('sensibilidade: ', sensibilidade)
print('especificidade: ', especificidade)
print('especificidade: ', especificidade2)


sns.set_theme(font_scale=1.5)
sns.heatmap(matrizConfusao, annot=True, cbar=False, xticklabels=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], yticklabels=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], fmt='.0f')
plt.ylabel('Real')
plt.xlabel('predita')
plt.show()