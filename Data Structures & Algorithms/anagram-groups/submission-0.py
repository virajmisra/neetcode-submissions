class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        m = {}
        for s in strs:
            sort = "".join(sorted(s))
            if sort not in m.keys():
                l = [s]
                m[sort] = l
            else:
                l = m[sort]
                l.append(s)
                m[sort] = l
        for l in m.values():
            res.append(l)
        return res


        