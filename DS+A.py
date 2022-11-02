
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) -1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i,j])
    # a dictionary will store the numbers
    # this is a faster run time however it takes up more memory considering numbers are stored
    def twoSumDictionary(self,nums,target):
        # this is how a dictionary is declared
        seen = {}
        # enumerate gets index and number value at the same time
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target-num],i])
            elif num not in seen:
                seen[num] = i


# make the class a obj
solved = Solution()
arr = [1,2,3,4]
target = 6
