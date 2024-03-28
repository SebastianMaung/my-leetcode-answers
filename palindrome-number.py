class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = []
        for i in range (len(str(x))):
            nums.append(str(x)[i])
        return nums == nums[::-1]
        

