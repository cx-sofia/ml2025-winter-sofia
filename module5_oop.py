class IntList():
  def __init__(self, n):
    self.n = n
    self.nums = []

  def add(self, num):
    if len(self.nums) < self.n:
      self.nums.append(num)
    else:
      raise IndexError("Redundant Number")

  def get_index(self, target):
    if target in self.nums:
      return self.nums.index(target) + 1
    return -1


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
