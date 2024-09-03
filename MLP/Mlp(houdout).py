import numpy as np
import pandas as pd
#from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
# from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import recall_score, f1_score, precision_score

#data = load_iris()
data = load_breast_cancer()
# data = load_digits()
xDF = pd.DataFrame(data.data, columns=data.feature_names)
xDF['target'] = data.target

X = xDF.drop('target', axis=1)
Y = xDF['target']

#separação treino/teste
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33,
#                                                     random_state=42)
# print('lenght: ', len(X_train))
# print('lenght: ', len(X_test))

accuracies = []

normalizer = MinMaxScaler()
X_norm = normalizer.fit_transform(X)    #só no x train.

print(X_norm)

#Multilayer Perceptron
for index in range(10):
    X_train, X_test, Y_train, Y_test = train_test_split(X_norm, Y, test_size=0.33,
                                                    random_state=index)
    
    data_classifier = MLPClassifier(random_state=1, max_iter=300).fit(X_train, Y_train)

    Y_pred = data_classifier.predict(X_test)

    accuracies.append(accuracy_score(Y_test, Y_pred))

mean_accuracie = sum(accuracies) / 10
print(f"mean accuracie = {mean_accuracie:.3f}")

matrizConfusao = confusion_matrix(Y_test, Y_pred)
print(matrizConfusao)

acuracia = accuracy_score(Y_test, Y_pred)
precisao = precision_score(Y_test, Y_pred)
sensibilidade = recall_score(Y_test, Y_pred)
f1 = f1_score(Y_test, Y_pred)

vn, fp, fn, vp = matrizConfusao.ravel()
especificidade = vn/(vn+fp)
especificidade2 = recall_score(Y_test, Y_pred, pos_label=0)

print('acuracia: ', acuracia)
print('precisao: ', precisao)
print('sensibilidade: ', sensibilidade)
print('especificidade: ', especificidade)

sns.set_theme(font_scale=1.5)
sns.heatmap(matrizConfusao, annot=True, cbar=False, xticklabels=['negativo', 'positivo'], yticklabels=['negativo', 'positivo'], fmt='.0f')
plt.ylabel('Real')
plt.xlabel('predita')
plt.show()