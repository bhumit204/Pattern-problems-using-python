"""
Pattern-7: Star Pyramid

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
  *  
 *** 
*****   
Input Format: N = 6
Result:
     *     
    ***    
   *****   
  *******  
 ********* 
***********

"""

def Star_Pyramid(N):
    for indx in range(1, N + 1):
        print((" " * (N - indx)) + ("*" * (2*indx - 1)))

N = int(input("Enter Positive nunber:"))
Star_Pyramid(N)