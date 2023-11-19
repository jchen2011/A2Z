# Given an integer N, print the following pattern :
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
class Solution:
    def printStars(n):
        for i in range(n):
            for j in range(n - i):
                print(j + 1, end="")
            print("")
    printStars(5)