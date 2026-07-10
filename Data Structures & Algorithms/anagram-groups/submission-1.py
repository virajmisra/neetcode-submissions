class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        res = []
        for s in strs:
            c = "".join(sorted(s))
            if c in m.keys():
                m[c].append(s)
            else:
                m[c] = []
                m[c].append(s)
        for k in m.keys():
            res.append(m[k])
        return res