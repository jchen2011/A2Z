# Given an integer N, print the following pattern :
# *
# **
# ***
# ****
# *****

class Solution:
    def printStars(n):
        for i in range(n):
            for j in range(i + 1):
                print("*", end="")
            print("")