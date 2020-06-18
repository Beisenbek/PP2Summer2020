#1 + 2 + 3 + 4 + +... + n
def rec(currentValue, biggestValue):
  if currentValue == biggestValue: return biggestValue
  return currentValue + rec(currentValue + 1, biggestValue)

print(rec(1, 10))