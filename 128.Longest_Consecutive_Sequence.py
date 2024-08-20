'''Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
### Idea: if we sort a list of integers and inspect the elements in the sorted version, we see that 
### consecutive element differ by +1 or -1. Thus for every element x in the list we check if there exists an
### element x-1 or x+1. If it does exist, we update the counter. We don't use count if a number is being 
### repeated again in the list

input = [100,4,200,1,3,2]
class Solution:
    def longestConsecutive(self, nums:list) -> int:
        count = 0 # Counter 

        for idx,num in enumerate(nums):
            if nums[idx:len(nums)].count(num)>1:
                continue
            if (num-1) in nums or (num+1) in nums:
                count += 1

sol = Solution()
sol.longestConsecutive(input)