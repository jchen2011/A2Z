# Given an integer N, print the following pattern :
# * * * * *
# * * * *
# * * *
# * *
# *

class Solution:
    def printStars(n):
        for i in range(n):
            for j in range(n - i):
                print("*", end="")
            print("")

    printStars(6)