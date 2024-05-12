"""
Pattern-5: Inverted Right Pyramid

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
* * *
* * 
*

Input Format: N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 

"""

def Inverted_Right_Pyramid(N):
    for indx in range(N, 0, -1):
        print(f"* " * indx)


N = int(input("Enter Positive Number:"))
Inverted_Right_Pyramid(N)