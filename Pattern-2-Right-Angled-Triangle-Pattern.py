"""
Pattern-2: Right-Angled Triangle Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
* 
* * 
* * *

Input Format: N = 6
Result:
* 
* * 
* * *
* * * *
* * * * *
* * * * * *

"""

def Right_Angled_Triangle_Pattern(N):
    for indx in range(1, N + 1):
        print("* "*indx)


N = int(input("Enter Positive Number:"))
Right_Angled_Triangle_Pattern(N)