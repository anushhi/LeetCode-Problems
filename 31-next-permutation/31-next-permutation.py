class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #for example take = [0,1,2,10,9,4,3]
        
        l = len(nums)
        
        #if there are three elements only then just reverse the number
        if l <=2:
            return nums.reverse()
        pointer = l - 2
        
        #this loop is tom find the breaking point of descendants i.e 2 here 
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1
        
        #in case the array is [3,2,1] then we will reach to a exausted condition then 
        #next permutation will be the first i.e [1,2,3]
        if pointer == -1:
            return nums.reverse()
        
        #if we are at some point then we will first swap the no with the next greater and then               #reverse it
        for i in range(l-1,pointer,-1):
            if nums[i] > nums[pointer]:
                nums[pointer],nums[i] = nums[i],nums[pointer]
                break
        
        nums[pointer+1:] = reversed(nums[pointer+1:])
        
        return nums
            
        
        
        