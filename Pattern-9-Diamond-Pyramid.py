"""
Pattern-9: Diamond Pyramid

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
  *   
 ***
***** 
*****  
 ***
  *   
Input Format: N = 6
Result:   
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *

"""

def Diamond_Pyramid(N):
    for indx in range(-N, N + 1):
        if indx < 0:
            indx = abs(indx)
        elif indx == 0:
            continue
        print((" " * (indx - 1)) + ("*" * ((2*N + 1)-2*indx)))

N = int(input("Enter Positive Number:"))
Diamond_Pyramid(N)