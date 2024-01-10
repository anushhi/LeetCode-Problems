class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #BruteForce
#         answer = []
#         for i in range(len(nums)):
#             temp_ans = 1
#             for j in range(len(nums)):
#                 if i != j:
#                     temp_ans *= nums[j]
                
#             answer.append(temp_ans)
                
#         return answer
        #optimisedApproach
        total_prod = 1
        flag = False
        for i in range(len(nums)):
            if nums[i] != 0:
                total_prod *= nums[i]
            elif flag == False:
                flag = True
            else:
                return [0]*len(nums)
            
        answer = []   
        for i in range(len(nums)):
            if nums[i] != 0:
                if flag == True:
                    answer.append(0)
                else:
                    answer.append(total_prod//nums[i])
            else:
                answer.append(total_prod)
            
        return answer
        
        
            