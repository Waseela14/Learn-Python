#   '''In order to ovoid overfitting and underfitting we use diffrent values of k 
#   to check for which value of k model predict best output'''

# import numpy as np

# train_accuracies = {}
# test_accuracies = {}
# neighbors = np.arange[1, 26]

# for neighbor in neighbors:
#     knn = KNeighborsClassifier(n_neighbors = neighbor)
#     knn.fit(x_train, y_train)
#     train_accuracies[neighbor] = knn.score(x_train, y_train)
#     test_accuracies[neighbor]  = knn.score(x_test, y_test)