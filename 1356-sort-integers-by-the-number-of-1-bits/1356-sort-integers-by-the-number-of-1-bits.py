class Solution:
    
    #Approach :- 1
        #Hamming Weight using built in method
        
    # def sortByBits(self, arr: List[int]) -> List[int]:
    #     arr.sort(key= lambda num: (num.bit_count(),num))
    #     return arr
        
    #Approach :- 2
        #Hamming Weight Bit Manipulation
    def sortByBits(self, arr: List[int]) -> List[int]:
        def findWeight(num):
            mask = 1
            weight = 0
            while num:
                if num & mask:
                    weight += 1
                    num ^= mask
                    
                mask <<= 1
            return weight
        
        arr.sort(key= lambda num: (findWeight(num),num))
        return arr                