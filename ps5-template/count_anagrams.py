import math

def count_anagrams(strings):
    "Return the number of pairs of anagrams in a tuple of strings"

    convert = {'x': 89, 'n': 43, 'e': 11, 'c': 5, 'm': 41, 'y': 97, 'i': 23, 'h': 19, 's': 67, 't': 71, 'k': 31, 'r': 61, 'b': 3,
               'a': 2, 'd': 7, 'g': 17, 'j': 29, 'z': 101, 'f': 13, 'w': 83, 'p': 53, 'u': 73, 'o': 47, 'q': 59, 'l': 37, 'v': 79}
    used = set()
    anagram = {}
    total = 0

    for word in strings:
        h_val = 1

        if word not in used:
            for let in word:
                h_val *= convert[let]

            if h_val in anagram:
                anagram[h_val] += 1
            else:
                anagram[h_val] = 1
        used.add(word)

    for val in anagram:
        if anagram[val] > 1:
            total += math.factorial(anagram[val])/(2 * math.factorial(anagram[val]-2))

    return int(total)