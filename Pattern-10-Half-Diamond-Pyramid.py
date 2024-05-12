"""
Pattern-10: Half Diamond Pyramid

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
  *
  **
  ***
  **
  *
Input Format: N = 6
Result:   
     *
     **
     ***
     ****
     *****
     ******
     *****
     ****
     ***
     **
     *

"""

def Half_Diamond_Pyramid(N):
    for indx in range(-N+1, N):
        if indx < 0:
            indx = abs(indx)
        print((" " * (N - 1)) + ("*" * (N - indx)))

N = int(input("Enter Positive Number:"))
Half_Diamond_Pyramid(N)