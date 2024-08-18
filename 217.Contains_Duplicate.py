class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dictionary = {}
        for number in nums:
            if str(number) in dictionary:
                return True
            dictionary[str(number)] = number
        return False
                

class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
    
nums=[1,2,3,4]
my_instance = Solution()
my_instance.containsDuplicate(nums)