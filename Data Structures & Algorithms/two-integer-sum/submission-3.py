class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            differ = target - nums[i]
            if differ in nums:
                j = nums.index(differ)
                if i != j:
                    return sorted([i, j])