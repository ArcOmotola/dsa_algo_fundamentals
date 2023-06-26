#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


def groupAnagrams(strs):
  anagram_groups = {}

  for word in strs:
    sorted_word = "".join(sorted(word))

    if sorted_word in anagram_groups:
      anagram_groups[sorted_word].append(word)
    
    else:
      anagram_groups[sorted_word] = [word]

  return anagram_groups.values()


words= ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(words)) 




#Time Complexity: The solution iterates over each word in the input array once and performs sorting operations on each word. Sorting a word takes O(k log k) time, where k is the length of the word. Therefore, the overall time complexity of the solution is O(n * k log k), where n is the number of words in the input array and k is the average length of the words.

#Space Complexity: The solution uses a dictionary (anagram_groups) to store the anagram groups. In the worst case, where all the words are unique and have no anagrams, the dictionary will store n key-value pairs. Therefore, the space complexity of the solution is O(n) for the dictionary.






#Performance Optimization: Is there any way to optimize the solution further? One optimization could be to use a default dictionary with a list as the default value. This way, we can avoid the conditional check for key existence when adding words to the anagram groups. Instead of checking if sorted_word is already a key, we can directly append the current word to anagram_groups[sorted_word]. This would simplify the code and potentially improve performance.
from collections import defaultdict

def groupAnagrams(strs):
    anagram_groups = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    
    return list(anagram_groups.values())
