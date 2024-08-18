# Case 1: True anagram, same number of letters, same letters ["anagram", "nagaram"]
# Case 2: Not anagram, same number of letters, different letters ["aaca", "ccaa"]
# Case 3: Not anagram, different number of letters, same letters ["aa", "a"]
# Case 4: Not anagram, different number of letters, different letters ["ab", "c"]

class Solution(object): 
    # Time complexity O(s+t) 
    # Memory complexity O(s+t) 
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictionary = {}
        dictionary_1 = {}
        for letter in s:
            if letter not in dictionary:
                dictionary.update({letter:1})
            else:
                dictionary[letter] += 1
        for letter in t:
            if letter not in dictionary_1:
                dictionary_1.update({letter:1})
            else:
                dictionary_1[letter] += 1
        return dictionary == dictionary_1
    
new_instance = Solution()
new_instance.isAnagram(s = "aa", t = "a")




class Solution_2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)



instance = Solution_2()
instance.isAnagram(s = "aacc", t = "ccac")

