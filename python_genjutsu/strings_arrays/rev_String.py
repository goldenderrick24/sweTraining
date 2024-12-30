from __future__ import division

class ReverseString(object):
    """
    Since Python strings are immutable, we'll use a list of chars instead to exercise in-place string manipulation as you would get with a C string.

    Iterate len(string)/2 times, starting with i = 0:
    Swap i and len(string) - 1 - i
    Increment i
    
    """
    def reverse(self, chars):
        if chars is None or not chars:
            return chars
        
        size = len(chars)
        for i in range(size//2):
            chars[i], chars[size-1-i] = chars[size-1-i], chars[i]
        return chars
    
    def reverse_string_alt(string):

        if string is None or not string:

            return string

        return string[::-1]


    def reverse_string_alt2(string):

        if string is None or not string:

            return string

        return ''.join(reversed(string))