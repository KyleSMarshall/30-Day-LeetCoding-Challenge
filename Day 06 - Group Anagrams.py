# Problem:
'''
Given an array of strings, group anagrams together.

Example - 
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]
'''

' -- There are two solutions below - my first (inefficient) solution and my second (optimized) solution.-- '


# Solution 2:
'''
My second solution made use of dictionaries and was very efficient.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    '''
    Groups anagrams together in a list.
    Sorts the characters in a word and checks if that sorted word is a key the dictionary named anagrams.
    If it is, the key has the original word appended to its value list.
    If it is not, the key has a list containing only the original word assigned to its value.
    '''
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return anagrams.values()
        
        
# Solution 1:
'''
My first solution made use of lists of anagrams and the sorted version of the anagram. This did pass all the test
cases within the alloted time, however it was terribly inefficient.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Obtain the length of all the words so we can find out the longest word
        str_lens = [len(word) for word in strs]
        max_str = max(str_lens)
        
        # Create two arrays, one containing the singular sorted anagram, and another containing the words that fit the anagram
        sorted_anagrams = [[] for i in range(0, max_str+1)]
        anagrams = [[] for i in range(0, max_str+1)]
        
        # Loop over all words and check if they match with an already seen sorted anagram. If not, add the new sorted anagram.
        for i in range(len(strs)):
            word = strs[i]
            n = len(word)
            check_word = ''.join(sorted(word))
            for j in range(len(sorted_anagrams[n])):
                if check_word == sorted_anagrams[n][j]:
                    # Matches with prev. seen anagram - > Add word to anagram group
                    anagrams[n][j].append(word)
                    break
            else:
                # No match so add sorted anagram to list and add word to a new anagram list
                sorted_anagrams[n].append(check_word)
                anagrams[n].append([word])
        
        # Only retrieve the non-empty elements
        anagrams = [item for sublist in anagrams for item in sublist if sublist != []]
        return anagrams
