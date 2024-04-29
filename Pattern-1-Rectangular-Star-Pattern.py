"""
Pattern-1: Rectangular Star Pattern

Problem Statement: Given an integer N, print the following pattern.

Example 1:
Input: N = 3
Output: 
* * *
* * *
* * *

Example 2:
Input: N = 6
Output:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

"""

def Rectangular_Star_Pattern(N):
    for indx in range(N):
        print("* "*N)


N = int(input("Enter Positive nunber:"))
Rectangular_Star_Pattern(N)