class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n,p,z = [],[],[]
        
        for num in nums:
            if num < 0:
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                z.append(num)
                
        N,P = set(n),set(p)
        
        if len(z) >= 3:
            res.add(tuple([0,0,0]))
            
        if z:
            for ele in P:
                if -1*ele in N:
                    res.add(tuple([-1*ele,0,ele]))
        
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([target,n[i],n[j]])))
                    
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
                    
        return res
        
                
        
            
        
        