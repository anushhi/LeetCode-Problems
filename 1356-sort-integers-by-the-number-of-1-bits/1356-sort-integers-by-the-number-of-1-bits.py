class Solution:
    
    #Approach :- 1
        #Hamming Weight usning built in method
        
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key= lambda num: (num.bit_count(),num))
        return arr
        