class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    #bruteforce 
        # for i in range (len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         sum = nums[i]+nums[j]
        #         if sum == target:
        #             return [i,j]
        
#         comp = dict()
        
#         for i in range(len(nums)):            #Moderate   
#             num = nums[i]
#             c = target - num
            
#             if nums[i] in comp:
#                 return [comp[num],i]
#             else: 
#                 comp[c] = i
                
        h = {}                              #optimal 
        for i , num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n] , i]



class MySolution:
    def twoSum(self, nums, target):
        h = {}                            
        for i , num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n] , i]
a = [2,1,3,2,4]
b = 7
x = MySolution()      

print (x.twoSum(a,b))





