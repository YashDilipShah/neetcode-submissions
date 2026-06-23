class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagrams = {}
        for s in range(len(strs)):
            sorted_cur = "".join(sorted(strs[s]))
            if sorted_cur in sorted_anagrams:
                sorted_anagrams[sorted_cur].append(s)
            else:
                sorted_anagrams[sorted_cur] = [s]
        ans = []
        for k in sorted_anagrams:
            ans.append([strs[idx] for idx in sorted_anagrams[k]])
        return ans
