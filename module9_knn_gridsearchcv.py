from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


def knn_classification_accuracy(x_train, y_train, x_test, y_test, k):
  model = KNeighborsClassifier(n_neighbors=k)
  model.fit(x_train, y_train)
  y_pred = model.predict(x_test)
  return accuracy_score(y_test, y_pred)


def main():
  N = int(input("Enter the number of points N: "))
  x_train = np.zeros((N, 1))
  y_train = np.zeros(N, dtype=int)
  for i in range(N):
      tmp_input = input(f"Enter {i+1}-th point: ").split()
      x, y = float(tmp_input[0]), int(tmp_input[1])
      x_train[i, 0] = x
      y_train[i] = y

  M = int(input("Enter the number of points M: "))
  x_test = np.zeros((M, 1))
  y_test = np.zeros(M, dtype=int)
  for i in range(M):
      tmp_input = input(f"Enter {i+1}-th point: ").split()
      x, y = float(tmp_input[0]), int(tmp_input[1])
      x_test[i, 0] = x
      y_test[i] = y

  best_k = 0
  best_accuracy = -1
  for k in range(1, 11):
      accuracy = knn_classification_accuracy(x_train, y_train, x_test, y_test, k)
      if accuracy > best_accuracy:
          best_accuracy = accuracy
          best_k = k
  print(f"Best k for the kNN Classification method is: {best_k}")
  print(f"Corresponding test accuracy is: {best_accuracy:.4f}")


if __name__ == "__main__":
  main()
