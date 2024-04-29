"""
Pattern-19: Symmetric-Void Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
******
**  **
*    *
*    *
**  **
******

Input Format: N = 6
Result:   
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************

"""

def Symmetric_Void_Pattern(N):
    for indx in range(-N, N + 1):
        if indx < 0:
            indx = abs(indx)
        elif indx == 0:
            continue
        pattern = ('*' * indx) + (" " * (N - indx))
        print(pattern + pattern[::-1])

N = int(input("Enter Positive nunber:"))
Symmetric_Void_Pattern(N)