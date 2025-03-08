from sklearn.metrics import precision_score, recall_score
import numpy as np


def get_precision_recall_binary(y_true, y_pred):
  precision = precision_score(y_true, y_pred, zero_division=0))
  recall = recall_score(y_true, y_pred, zero_division=0))
  return precision, recall


def main():
  N = int(input("Enter the number of points N: "))

  x_array = np.zeros(N)
  y_array = np.zeros(N)
  for i in range(N):
      x, y = [float(c) for c in input(f"Enter {i+1}-th point: ").split()]
      if x not in [0, 1] or y not in [0, 1]:
        raise ValueError("Both X and Y are either 0 or 1.")
      x_array[i] = x
      y_array[i] = y
  
  precision, recall = get_precision_recall_binary(x_array, y_array)
  print(f"Precision is: {precision:.4f}")
  print(f"Recall is: {recall:.4f}")


if __name__ == "__main__":
  main()
