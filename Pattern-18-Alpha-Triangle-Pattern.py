"""
Pattern-18: Alpha-Triangle Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
C
B C
A B C

Input Format: N = 6
Result:   
F
E F
D E F
C D E F
B C D E F
A B C D E F

"""

def Alpha_Triangle_Pattern(N):
    pattern = ''
    for indx in range(64 + N, 64, -1):
        pattern = f"{chr(indx)} " + pattern
        print(pattern)

N = int(input("Enter Positive nunber:"))
Alpha_Triangle_Pattern(N)