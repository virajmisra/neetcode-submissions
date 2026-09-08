class TimeMap:

    def __init__(self):
        self.store = {}
        # list of tuples : key, [[value, timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        res = ""
        values = self.store[key]

        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l+r) // 2

            time = values[m][1]

            if time <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

        
