class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_s = {}
        if len(s) != len(t):
            return False
        for i in range(0, len(s)):
            if s[i] not in anagram_s:
                anagram_s[s[i]] = 1
            else:
                anagram_s[s[i]] = anagram_s[s[i]] + 1
        for i in range(0, len(t)):
            if t[i] not in anagram_s:
                return False
            else:
                anagram_s[t[i]] = anagram_s[t[i]] - 1
            if anagram_s[t[i]] < 0:
                return False
        for i in anagram_s:
            if anagram_s[i] != 0:
                return False
        return True
