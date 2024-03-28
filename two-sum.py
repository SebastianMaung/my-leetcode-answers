class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test = []
        for i in range(len(nums)):
            for y in range(len(nums)):
                if nums[i]+nums[y]==target and i != y:
                    return(i, y)
        return(test)

