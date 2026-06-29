class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        res = []
        for query in queries:
            left = query[0]
            right = query[1]

            total = 0
            for k in range(left, right + 1):
                current_word = words[k]
                l = 0
                r = len(current_word) - 1
                if current_word[l] in vowels and current_word[r] in vowels:
                    total += 1
            res.append(total)
        return res
