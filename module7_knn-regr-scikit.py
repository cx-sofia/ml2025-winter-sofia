from sklearn.neighbors import KNeighborsRegressor
import numpy as np


def knn_regression(x_train, y_train, X, k):
  model = KNeighborsRegressor(n_neighbors=k)
  model.fit(x_train, y_train)
  
  return model.predict(np.array([[X]]))[0]


def main():
  N = int(input("Enter the number of points N: "))
  k = int(input("Enter k: "))
  if k > N:
    raise ValueError("k must be less than or equal to N.")

  x_array = np.zeros((N, 1))
  y_array = np.zeros(N)
  for i in range(N):
      x, y = [float(c) for c in input(f"Enter {i+1}-th point: ").split()]
      x_array[i, 0] = x
      y_array[i] = y

  X = float(input("Enter the input X: "))
  
  result = knn_regression(x_array, y_array, X, k)
  variance = np.var(y_array)
  print(f"Predicted Y value for X = {X} is: {result}")
  print(f"Variance of labels in the training dataset is: {variance}")


if __name__ == "__main__":
  main()
