from collections import defaultdict
# Hashmap idx: letters
Input = [["act","pots","tops","cat","stop","hat"],
         [""],
         ["a"]]

Output = [[["hat"],["act", "cat"],["stop", "pots", "tops"]],
          [""],
          ["a"]]


def groupAnagrams(strs = None):
    output_list = []
    word_dict = {}
    for idx, word in enumerate(strs):
        letters = list(word)
        letters.sort()
        letters = str(letters)
        if letters in word_dict.keys():
            word_dict[letters].append(word)
        else:
            word_dict[letters] = [word]
    output_list = list(word_dict.values())
    return output_list

def groupAnagramsOptimised(strs = None):
    res = defaultdict(list) # We are mapping charCount to the list of anagrams

    for s in strs: # For every word in the given list of words
        count = [0] * 26 # start counting how many times each letter appears
        
        for c in s: # For every letter of the word
            count[ord(c) - ord('a')] += 1 # Add 1 to position corresponding to the letter 
        res[tuple(count)].append(s) 

        return res.values()

for idx, input in enumerate(Input):
    res_1 = [sorted(groupAnagrams(strs = input)), sorted(list(groupAnagramsOptimised(strs = input)))]
    res_2 = [[sorted(Output[idx])],[sorted(list(Output[idx]))]]

    try:
        assert res_1[0] == res_2[0], f"Function output {groupAnagrams(strs=input)} is not equal to the output {Output[idx]}"
        # assert res_1[1] == res_2[1], f"Function output {groupAnagramsOptimised(strs=input)} is not equal to the output {Output[idx]}"
        print("All tests passed")
        
    except AssertionError as e:
        print(e)
