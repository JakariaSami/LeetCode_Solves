class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    collection = set()
    res = 0

    for r in range(len(s)):
      while s[r] in collection:
        collection.remove(s[l])
        l += 1
      collection.add(s[r])
      res = max(res, r - l + 1)

    return res
