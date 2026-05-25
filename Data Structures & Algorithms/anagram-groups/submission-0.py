class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = defaultdict(list)
        for i in strs:
            sortedStr = ''.join(sorted(i))
            op[sortedStr].append(i)
        return list(op.values())