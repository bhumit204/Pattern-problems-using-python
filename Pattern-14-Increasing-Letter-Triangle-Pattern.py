"""
Pattern-14: Increasing Letter Triangle Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
A
A B
A B C

Input Format: N = 6
Result:   
A
A B
A B C
A B C D
A B C D E
A B C D E F

"""

def Increasing_Letter_Triangle_Pattern(N):
    strng = ''
    for indx in range(65, 65 + N):
        strng += f"{chr(indx)} "
        print(strng)

N = int(input("Enter Positive nunber:"))
Increasing_Letter_Triangle_Pattern(N)