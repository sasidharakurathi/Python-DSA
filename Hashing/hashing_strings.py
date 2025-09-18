
#   since strings are immutable objects, we can hash the strings to find out there frequencies. (Ex: Anagrams problem)
from collections import defaultdict

words = ["bat", "tab", "cat", "act"]
anagrams = defaultdict(list)    # creating a default dictionary of list as default value.

for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)

# print(dict(anagrams))
print(list(anagrams.values()))