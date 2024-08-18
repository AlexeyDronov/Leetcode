Inputs = [
    ([1,1,1,2,2,3], 2),
    ([1], 1)
]
Outputs = [
    [1,2],
    [1]
]

def top_K_frequent(nums,k):
    # [1,1,1,2,2,3] -> [1,2]
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    freq_sorted = sorted(freq.items(), key=lambda x:x[1])
    result = []
    for i in range(k):
        result.append(freq_sorted[-k:][i][0])
    return result

def top_K_frequent_opt(nums,k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


for idx, input in enumerate(Inputs):
    try:
        #top_K_frequent(nums=input[0], k=input[1])
        top_K_frequent_opt(nums=input[0], k=input[1])
        #assert top_K_frequent(nums=input[0], k=input[1]) == Outputs[idx], f"Function output {top_K_frequent(nums=input[0], k=input[1])} not equal {Outputs[idx]}"
    except AssertionError as e:
        # print(e)    
        pass