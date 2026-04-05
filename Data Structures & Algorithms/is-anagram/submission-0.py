class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_s = {}
        anagram_t = {}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in anagram_s:
                anagram_s[i] = 1
            else:
                anagram_s[i] = anagram_s[i] + 1
        for i in t:
            if i not in anagram_t:
                anagram_t[i] = 1
            else:
                anagram_t[i] = anagram_t[i] + 1     
        for c in anagram_s:
            if anagram_s[c] != anagram_t.get(c, 0):
                return False
        return True        