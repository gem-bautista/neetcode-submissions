class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        prefix = [0] * (len(words) + 1)
        prev = 0
        res = []

        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prev += 1
            prefix[i + 1] = prev

        for query in queries:
            l, r = query
            total = prefix[r + 1] - prefix[l]
            res.append(total)

        return res
