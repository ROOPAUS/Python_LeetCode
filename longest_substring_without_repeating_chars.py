class Solution:
    def lengthOfLongestSubstring(self, s):
        charMap = {}
        # set initial values in charmap as -1
        # LOGIC:If value is -1 for any character in a string, it means that character hasnt occured yet in the string
        for i in range(256):
            charMap[i] = -1
            i = 0
            max_len = 0
        for j in range(len(s)):
            # when charMap[ord(s[j])] >= i, it means that a character is getting repeated. 
            #So we need to update i.
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            current_len = j-i+1
            max_len = max(max_len, current_len)
        return max_len 
  
# Driver program to test the above function 
s = input("Enter string: ")
length = Solution().lengthOfLongestSubstring(s) 
print ("The length of the longest non-repeating character" +
       " substring is " + str(length)) 
     