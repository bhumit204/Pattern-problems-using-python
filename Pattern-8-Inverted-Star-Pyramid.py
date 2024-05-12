"""
Pattern-8: Inverted Star Pyramid

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
*****  
 ***
  *   
Input Format: N = 6
Result:     
***********
 *********
  *******
   ***** 
    ***    
     *

"""

def Inverted_Star_Pyramid(N):
    for indx in range(N,0,-1):
        print((" " * (N - indx)) + ("*" * (2*indx - 1)))

N = int(input("Enter Positive Number:"))
Inverted_Star_Pyramid(N)