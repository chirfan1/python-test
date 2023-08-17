class Solution(object):
    def shuffle(self, nums, n):
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans

"""
:type nums: List[int]
:type n: int
:rtype: List[int]
"""
