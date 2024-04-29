"""
Pattern-15: Reverse Letter Triangle Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
A B C
A B
A

Input Format: N = 6
Result:   
A B C D E F
A B C D E 
A B C D
A B C
A B
A

"""

def Reverse_Letter_Triangle_Pattern(N):
    strng = ''
    pattern = ''
    for indx in range(65, 65 + N):
        strng += f"{chr(indx)} "
        pattern = strng + '\n' + pattern
    print(pattern)

N = int(input("Enter Positive nunber:"))
Reverse_Letter_Triangle_Pattern(N)