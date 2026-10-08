class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):
            for a in range(1, len(strs)):
                if i >= len(strs[a]) or strs[a][i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix