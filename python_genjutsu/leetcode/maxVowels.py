"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, 
return the maximum number of vowel 
letters in any substring of s with length k.


The sliding window approach tracks the number of vowels in 
a substring of size k. As the window slides, the count of 
vowels is adjusted dynamically by adding the new character 
and removing the character that leaves the window.

- Use a sliding window of size k.
- Maintain a count of vowels in the current window.
- Update the maximum count of vowels at each step as the window slides.
"""
def maxVowels(s,k):
    vowels = set('aeiou')
    maxCount = currentCount = 0
    for i in range(len(s)):
        if s[i] in vowels:
            currentCount +=1
        if i>=k and s[i-k] in vowels:
            currentCount -=1

    maxCount = max(maxCount, currentCount)
    return maxCount
        