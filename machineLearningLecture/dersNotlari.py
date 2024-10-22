# import numpy as np

# A = np.array([[4,2],[1,3]])

# eigenvalues,eigenvectors = np.linalg.eig(A)

# print("Özdeğerler: " , eigenvalues)
# print("Özvektörler: ",eigenvectors)

# import numpy as np 
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris

# iris = load_iris()

# X = iris.data
# X_meaned = X-np.mean(X,axis=0)


# cov_matris= np.cov(X_meaned,rowvar=False)
# eigenvalues,eigenvectors = np.linalg.eig(cov_matris)

# print("Özdeğerler: " , eigenvalues)
# print("Özvektörler: ",eigenvectors)

# # Adım 5: Özdeğerlerin sıralanması ve en yüksek iki özdeğerin seçilmesi
# sorted_index = np.argsort(eigenvalues)[::-1]  # büyükten küçüğe doğru sıralar
# sorted_eigenvalues = eigenvalues[sorted_index]
# sorted_eigenvectors = eigenvectors[:, sorted_index]

# # İlk iki bileşene karşılık gelen özvektörlerin seçilmesi
# n_components = 2
# eigenvector_subset = sorted_eigenvectors[:, :n_components]

# # Adım 6: Verinin seçilen özvektörler ile boyut indirgeme işlemi
# X_reduced = np.dot(X_meaned, eigenvector_subset)

# # Adım 7: Sonuçların görselleştirilmesi
# plt.figure(figsize=(8, 6))
# for i in range(len(iris.target_names)):
#     plt.scatter(X_reduced[iris.target == i, 0],
#                 X_reduced[iris.target == i, 1],
#                 label=iris.target_names[i])

# plt.xlabel('Principal Component 1')
# plt.ylabel('Principal Component 2')
# plt.title('PCA on Iris Dataset (Manually Computed)')
# plt.legend()
# plt.show()


# import numpy as np 
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
# from sklearn.decomposition import PCA

# iris = load_iris()

# X = iris.data
# Y= iris.target

# pca=PCA(n_components=2)
# X_pca=pca.fit_transform(X)


# # Adım 7: Sonuçların görselleştirilmesi
# plt.figure(figsize=(8, 6))
# for i in range(len(iris.target_names)):
#     plt.scatter(X_pca[iris.target == i, 0],
#                 X_pca[iris.target == i, 1],
#                 label=iris.target_names[i])

# plt.xlabel('Principal Component 1')
# plt.ylabel('Principal Component 2')
# plt.title('PCA on Iris Dataset (Manually Computed)')
# plt.legend()
# plt.show()


# LDA kısmı


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Adım 1: Iris veri setinin yüklenmesi
# iris = load_iris()
# X = iris.data
# y = iris.target

# # Adım 2: Sınıfların ortalama vektörlerinin hesaplanması
# mean_vectors = []
# for cl in np.unique(y):
#     mean_vectors.append(np.mean(X[y == cl], axis=0))

# # Adım 3: Sınıf içi yayılım matrisinin hesaplanması (S_W)
# S_W = np.zeros((X.shape[1], X.shape[1]))
# for cl, mean_vec in zip(np.unique(y), mean_vectors):
#     class_sc_mat = np.zeros((X.shape[1], X.shape[1]))  # Sınıf içi scatter matrix
#     for row in X[y == cl]:
#         row, mean_vec = row.reshape(X.shape[1], 1), mean_vec.reshape(X.shape[1], 1)
#         class_sc_mat += (row - mean_vec).dot((row - mean_vec).T)
#     S_W += class_sc_mat


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris

# # Adım 1: Iris veri setinin yüklenmesi
# iris = load_iris()
# X = iris.data
# y = iris.target

# # Adım 2: Sınıfların ortalama vektörlerinin hesaplanması
# mean_vectors = []
# for cl in np.unique(y):
#     mean_vectors.append(np.mean(X[y == cl], axis=0))

# # Adım 3: Sınıf içi yayılım matrisinin hesaplanması (S_W)
# S_W = np.zeros((X.shape[1], X.shape[1]))
# for cl, mean_vec in zip(np.unique(y), mean_vectors):
#     class_sc_mat = np.zeros((X.shape[1], X.shape[1]))  # Sınıf içi scatter matrix
#     for row in X[y == cl]:
#         row, mean_vec = row.reshape(X.shape[1], 1), mean_vec.reshape(X.shape[1], 1)
#         class_sc_mat += (row - mean_vec).dot((row - mean_vec).T)
#     S_W += class_sc_mat

# # Adım 4: Sınıflar arası yayılım matrisinin hesaplanması (S_B)
# overall_mean = np.mean(X, axis=0).reshape(X.shape[1], 1)
# S_B = np.zeros((X.shape[1], X.shape[1]))
# for i, mean_vec in enumerate(mean_vectors):
#     n = X[y == i, :].shape[0]  # Her sınıftaki örnek sayısı
#     mean_vec = mean_vec.reshape(X.shape[1], 1)  # Sınıfın vektörü sütun vektörü haline getirildi
#     S_B += n * (mean_vec - overall_mean).dot((mean_vec - overall_mean).T)

# # Adım 5: Özdeğer ve özvektörlerin hesaplanması
# eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))

# # Adım 6: En yüksek özdeğerlere göre sıralama
# sorted_indices = np.argsort(eig_vals)[::-1]
# eig_vecs = eig_vecs[:, sorted_indices]

# # Adım 7: En yüksek 2 özvektörün seçilmesi ve verinin projekte edilmesi
# n_components = 2
# W = eig_vecs[:, :n_components]  # Projeksiyon matrisi
# X_lda = X.dot(W)  # Verinin projekte edilmesi

# # Adım 8: Verinin görselleştirilmesi
# plt.figure(figsize=(8, 6))
# for i, label in enumerate(np.unique(y)):
#     plt.scatter(X_lda[y == label, 0], X_lda[y == label, 1], label=f"Class {label}")
# plt.title("LDA ile Projeksiyon")
# plt.xlabel("LD1")
# plt.ylabel("LD2")
# plt.legend()
# plt.show()




import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



# Adım 1: Iris veri setinin yüklenmesi
iris = load_iris()
X = iris.data
y = iris.target


X_train, X_test, y_train, y_test =train_test_split(X,y, test_size=0.3,
                                                   random_state=42)

lda=LDA(n_components=2)
X_train_lda =lda.fit_transform(X_train, y_train)
X_test_lda=lda.transform(X_test)


# LDA sonucunu görselleştirme
plt.figure(figsize=(8, 6))
for i in range(len(iris.target_names)):
    plt.scatter(X_train_lda[y_train == i, 0],
                X_train_lda[y_train == i, 1],
                label=iris.target_names[i])

plt.xlabel('LDA Component 1')
plt.ylabel('LDA Component 2')
plt.title('LDA on Iris Dataset')
plt.legend()
plt.show()


# Adım 5: LDA ile sınıflandırma
lda_classifier = LDA()
lda_classifier.fit(X_train_lda, y_train)  # Dikkat: X_train ve y_train değişkenleri olmalı
y_pred = lda_classifier.predict(X_test_lda)

# Adım 6: Model doğruluğunun hesaplanması
accuracy = accuracy_score(y_test, y_pred)
print(f'LDA Sınıflandırma Doğruluğu: {accuracy:.2f}')

