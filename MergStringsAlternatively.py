#!/usr/bin/python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newString = ""
        a = True if len(word1) >= len(word2) else False
        if a:
            for x in range(0,len(word2)):
                newString += (word1[x])
                newString += (word2[x])
            for j in range(len(word2), len(word1)):
                newString += word1[j]
        elif not a:
            for x in range(0,len(word1)):
                newString += (word1[x])
                newString += (word2[x])
            for jj in range(len(word1), len(word2)):
                newString += word2[jj]
        return(newString)
