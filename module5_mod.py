class IntList():
  def __init__(self, n):
    self.n = n
    self.nums = []

  def add(self, num):
    if len(self.nums) < self.n:
      self.nums.append(num)
    else:
      raise Error("Redundant Number")

  def get_index(self, target):
    if target in self.nums:
      return self.nums.index(target) + 1
    return -1
