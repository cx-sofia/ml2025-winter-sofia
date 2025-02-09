def get_index(target, l):
  if target in l:
    return l.index(target) + 1
  return -1


def main():
  N = int(input("Enter the number of numbers N: "))
  
  numbers = []
  for i in range(N):
      num = int(input(f"Enter number {i+1}: "))
      numbers.append(num)
  
  X = int(input("Enter an integer X: "))

  print(get_index(X, numbers))


if __name__ == "__main__":
  main()
