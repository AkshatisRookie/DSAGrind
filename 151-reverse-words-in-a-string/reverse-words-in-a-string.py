class Solution:
    def reverseWords(self, s: str) -> str:
        string=s.split() #gives a list
        reverse=string[::-1]
        return " ".join(reverse) # joining with gaps
        


