'''
def are_anagrams(word1, word2):
    if word1 == word2:
        return False
    else:
        list1 = list(word1)
        list2 = list(word2)
        list1.sort()
        list2.sort()
        return list1 == list2
'''
def are_anagrams(word1, word2):
    if word1 == word2:
        return False
    else:
        return sorted(word1) == sorted(word1)