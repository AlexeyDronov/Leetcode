### ALGORITHM TO SOLVE THIS PROBLEM
### race a car -> raceacar -> [race], [acar] -> 
### [race], [raca] -> if not equal -> palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool: 
        s = s.casefold() # remove capital letters from the given string
        str_alpha = ''.join(ch for ch in s if ch.isalnum()) # remove all but alphanumeric characters
        
        half_len = int(len(str_alpha)/2) # get half length of the resulting string
        first_half = str_alpha[0:half_len] # get the first half of the string
        if len(str_alpha)%2 == 0: # if the length of the string is even 
            second_half_reversed = str_alpha[half_len::][::-1]
        else: # if it is odd
            second_half_reversed = str_alpha[(half_len+1)::][::-1]
        if first_half == second_half_reversed: # return true if palindrome
            print("True")
            return True
        else:
            print("False")
            return False

sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")
sol.isPalindrome("race a car")
sol.isPalindrome(" ")
sol.isPalindrome("0P")


