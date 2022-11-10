class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for string in s:
            if st and st[-1] == string:
                
                st.pop()
            else:
                st.append(string)
        return ''.join(st)
        