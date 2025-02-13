from module5_mod import IntList


def main():
  N = int(input("Enter the number of numbers N: "))
  int_list = IntList(n=N)
  
  for i in range(N):
      num = int(input(f"Enter number {i+1}: "))
      int_list.add(num)
  
  X = int(input("Enter an integer X: "))
  print(int_list.get_index(X))


if __name__ == "__main__":
  main()
