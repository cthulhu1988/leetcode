#!/usr/bin/python3

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        startingPoints = []
        leadingChar = str2[0]
        for x, char in enumerate(str1):
            if char == leadingChar:
                startingPoints.append(x)
        snippets = self.compareStrings(str1, str2, startingPoints)
        snip = "".join(snippets)
        print(snip)
    

    def compareStrings(self, str1:str, str2:str, startingPoints) -> str:
        list = set()
        for point in startingPoints:
            pace1 = 0
            pace2 = point
            while str1[pace2] == str2[pace1] and pace1 <= len(str2):
                list.add(str2[pace1])
                #print(str1[pace2], str2[pace1])
                pace1 += 1
                pace2 += 1
                if pace1 >= len(str2): 
                    pace1 = 0
                    break
                else: 
                    pace1
                
                if pace2 >= len(str1): 
                    break
            
                #print(str1[pace2], str2[pace1])
        return sorted(list)

sol = Solution()

#str1 = "ABCABC"
#str2 = "ABC"

str1 = "ABABAB"
str2 = "ABAB"

#str1 = "LEET"
#str2 = "CODE"

sol.gcdOfStrings(str1, str2)


