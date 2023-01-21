class Solution:
    # def reversePairs(self, nums: List[int]) -> int:
# Brute force with TC - O(N*2)
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] > nums[j]*2:
        #             count += 1
        # return count
        
        
        
    
# Optimal 

        
    def reversePairs(self,nums: List[int]) -> int:
        
        def merge(nums,low,mid,high):
            count = 0
            j = mid + 1
            
            for i in range(low,mid+1):
                while j<= high and nums[i] > nums[j]*2:
                    j += 1
                count += (j - (mid+1))
            temp = []
            left = low
            right = mid+1
        
            while(left<=mid and right<=high):
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right+= 1

            while left<=mid:
                temp.append(nums[left])
                left += 1

            while right<=high:
                temp.append(nums[right])
                right += 1

            for i in range(low,high+1):
                nums[i] = temp[i-low]

            return count
                
        
        
        def mergeSort(nums,low,high):
            if low >= high:
                return 0
            mid = (low+high)//2
            inv = mergeSort(nums,low,mid)
            inv += mergeSort(nums,mid+1,high)
            inv += merge(nums,low,mid,high)

            return inv
    
        return mergeSort(nums,0,len(nums)-1)
        

    
