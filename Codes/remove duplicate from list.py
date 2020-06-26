def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)

######################################################


t = [1, 2, 3, 1, 2, 5, 6, 7, 8]

a = list(set(t))

print(a)
######################################################

def removeDuplicates(self, nums: List[int]) -> int:     #returns length of the duplicate-free array
        # if len(nums) == 0:
        #     return 0 
        # if len(nums) == 1:
        #     return 1
        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        print (nums)
        return j + 1
      
      
