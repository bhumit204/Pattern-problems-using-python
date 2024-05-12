"""
Pattern-21: Hollow Rectangle Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
***
* *
***

Input Format: N = 6
Result:   
******
*    *
*    *
*    *
*    *
******

"""

def Hollow_Rectangle_Pattern(N):
    for indx in range(1, N + 1):
        if indx == 1 or indx == N:
            print('*' * N)
        else:
            print("*" + (" " * (N -2)) + "*")

N = int(input("Enter Positive Number:"))
Hollow_Rectangle_Pattern(N)