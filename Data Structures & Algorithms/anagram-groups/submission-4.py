class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ss = str(sorted(s))
            if ss not in d:
                d[ss] = []
            d[ss].append(s)
        res = []
        for s in d:
            words = []
            while d[s]:
                words.append(d[s].pop())
            res.append(words)
        return res
        