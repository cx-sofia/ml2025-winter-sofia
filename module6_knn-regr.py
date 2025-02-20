import numpy as np


def knn_regression_1d(x_array, y_array, X, k):
  indices = np.argpartition(np.abs(x_array - X), k)[:k]
  return np.mean(y_array[indices])


def main():
  N = int(input("Enter the number of points N: "))
  k = int(input("Enter k: "))
  if k > N:
    raise ValueError("k must be less than or equal to N.")

  x_array = np.zeros(N)
  y_array = np.zeros(N)
  for i in range(N):
      x, y = [float(c) for c in input(f"Enter {i+1}-th point: ").split()]
      x_array[i] = x
      y_array[i] = y

  X = float(input("Enter the input X: "))
  
  result = knn_regression_1d(x_array, y_array, X, k)
  print(f"Predicted Y value for X = {X} is: {result}")


if __name__ == "__main__":
  main()
