# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word = str(input("Please enter a word: "))
anagram = str(input("Please enter a second word: "))

def find_anagram(word, anagram):
    # [assignment] Add your code here

    if (sorted(word)==sorted(anagram)):
        print("True")
        return True
        
    else:
        print("False")
        return False

find_anagram(word,anagram)