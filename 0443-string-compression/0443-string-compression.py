class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 1
        left = 0
        for right in range(1,len(chars)+1):
            if right < len(chars) and chars[right-1] == chars[right]:
                cnt += 1
            else:
                chars[left] = chars[right-1]
                left += 1
                if cnt > 1:
                    for c in str(cnt):
                        chars[left] = c
                        left += 1
                cnt = 1
                    
                    
        return left

                