"""
Pattern-12: Number Crown Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1    1
12  21
123321

Input Format: N = 6
Result:   
1          1
12        21
123      321
1234    4321
12345  54321
123456654321
"""

def Number_Crown_Pattern(N):
    pos = ''
    for indx in range(1, N + 1):
        pos += str(indx)
        print(pos + (" " * (2 * (N - indx))) + pos[::-1])

N = int(input("Enter Positive Number:"))
Number_Crown_Pattern(N)