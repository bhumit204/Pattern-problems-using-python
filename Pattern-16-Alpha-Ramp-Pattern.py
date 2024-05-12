"""
Pattern-16: Alpha-Ramp Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
A
B B
C C C

Input Format: N = 6
Result:   
A 
B B
C C C
D D D D
E E E E E
F F F F F F

"""

def Alpha_Ramp_Pattern(N):
    letter = 64
    for indx in range(1,N+1):
        print(f"{chr(letter + indx)} " * indx)

N = int(input("Enter Positive Number:"))
Alpha_Ramp_Pattern(N)