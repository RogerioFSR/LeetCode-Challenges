class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # This solution is unoptimal, we could use a dictionary to store the indexes of numbers encountered.
        i = 0
        j = 1

        while (i < len(nums)):
            while(j < len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
                else:
                    j += 1
            i += 1
            j = i + 1

    def optimaltwoSum(self, nums: List[int], target: int) -> List[int]: # This would be a more optimal solution for this problem
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i