class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        ids = []
        res = [0] * len(temperatures)
        try:
            for idx in range(len(temperatures)):
                while days and days[-1] < temperatures[idx]:
                    res[ids[-1]] = idx - ids[-1]
                    days.pop()
                    ids.pop()
                days.append(temperatures[idx])
                ids.append(idx)
        except:
            return res
        return res
