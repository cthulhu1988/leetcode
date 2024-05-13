#!/usr/bin/python3

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        startingPoints = []
        leadingChar = str2[0]
        for x, char in enumerate(str1):
            if char == leadingChar:
                startingPoints.append(x)
        print(startingPoints)
