aList = [86, 96, 87, 58, 26, 10, 95, 56, 98, 14]

def findLargest(aList):
  largest = aList[0]
  for num in aList:
    if num > largest:
      largest = num
  return largest

def findSmallest(aList):
  smallest = aList[0]
  for num in aList:
    if num < smallest:
      smallest = num
  return smallest

def meanNoOutliers(aList):
  total = 0
  for num in aList:
    total += num
  total -= (findSmallest(aList) + findLargest(aList))
  return total / (len(aList) - 2)

def countValuesBetween(aList, min, max, incl):
  total = 0
  if incl == "true":
    for num in aList:
      if num >= min and num <= max:
        total += 1
    return total
  elif incl == "false":
    for num in aList:
      if num > min and num < max:
        total += 1
    return total

def noDuplicates(aList):
  ndx = 0
  for num1 in aList:
    while ndx < len(aList):
      return "true"