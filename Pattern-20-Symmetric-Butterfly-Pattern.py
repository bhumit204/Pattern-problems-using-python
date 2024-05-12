"""
Pattern-20: Symmetric-Butterfly Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
*    *
**  **
******
**  **
*    *


Input Format: N = 6
Result:   
*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *

"""

def Symmetric_Butterfly_Pattern(N):
    for indx in range(-N + 1, N):
        if indx < 0:
            indx = abs(indx)
        pattern = ('*' * (N - indx)) + (" " * indx)
        print(pattern + pattern[::-1])

N = int(input("Enter Positive Number:"))
Symmetric_Butterfly_Pattern(N)