import operator
from ast import JoinedStr


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    # when doing the problem break the input down to 1-3 items example if there is an input that has 5 items in list scale it down to 3 items instead
    # To test Big O(N) NOTATION/effiency scale the input to size of 100
    # I need to track the list I'm building and not inputs <<< BIG ISSUE of MINE

    # create an empty list --> anagram_list = []
    # use the input list and store each word in list as a key and set any value --> {"eat":1, "tea":1, "ten": 1}
    # check if the length of the string is the same and check if the word in the list -1 is the same as the current position. 
    # if both conditionals are satisfied then append else create new list
        # strings =["eat", "tea", "tan"]
        
    anagram_dict = {}
    for word in strings:
        sorted_char=sorted(word)
        joined_word=''.join(sorted_char)
        if joined_word in anagram_dict:
            anagram_dict[joined_word].append(word)
        else:
            anagram_dict[joined_word] = [word]
    anagram_list = []
    for key in anagram_dict.keys():
        anagram_list.append(anagram_dict[key])
    print(anagram_list)
    return anagram_list

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    nums_dict = {}
    print(nums)
    for i in range (len(nums)):

        if nums[i] in nums_dict:
            
            nums_dict[nums[i]] += 1
        else:
            nums_dict[nums[i]] = 1

    print(nums_dict)    
    frequency_list=[]
    # items =sorted((nums_dict.items()),key =operator.itemgetter(1), reverse =True)
    items = sorted(nums_dict, key=lambda x : nums_dict[x],reverse=True)     
    print(items, "items")

    for i in range (len(items)):
        if (len(frequency_list)) <k:
            frequency_list.append(items[i])

    print(frequency_list, "list")
    print(frequency_list[:k])
    return frequency_list


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    pass

