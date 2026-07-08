class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longer = max(len(word1), len(word2))
        shorter = min(len(word1), len(word2))
        merged_st = ""

        for i in range(longer):
            if i != shorter:
                merged_st += word1[i] + word2[i]
            else:
                if len(word1) == longer:
                    merged_st += word1[i : longer+1]
                    break
                else:
                    merged_st += word2[i: longer+1]
                    break
        
        return merged_st
            