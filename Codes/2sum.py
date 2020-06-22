class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range (len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         sum = nums[i]+nums[j]
        #         if sum == target:
        #             return [i,j]
        
        comp = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            c = target - num
            
            if nums[i] in comp:
                return [comp[num],i]
            else: 
                comp[c] = i
