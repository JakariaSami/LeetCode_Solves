class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for i in matrix:
      low = 0
      high = len(i) - 1

      while low <= high:
        mid = low + (high - low) // 2

        if target == i[mid]:
          return True
        elif i[mid] > target:
          high = mid - 1
        else:
          low = mid + 1

    return False
