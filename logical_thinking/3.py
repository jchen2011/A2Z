# Given an integer N, print the following pattern :
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

class Solution:
    def printStars(n):
        for i in range(n):
            for j in range(i + 1):
                print(j + 1, end="")
            print("")


    printStars(6)