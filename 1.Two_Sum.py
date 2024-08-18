#nums = [[2,7,11,15], [3,3], [3,2,4]]
#target = [9, 6, 6]

def two_sum(nums, target):
    hashMap = {} # val : idx
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in hashMap:
            return [hashMap[diff], idx]
        hashMap[val] = idx
    return

two_sum(nums=[2,4,3,5,5,11], target=10)