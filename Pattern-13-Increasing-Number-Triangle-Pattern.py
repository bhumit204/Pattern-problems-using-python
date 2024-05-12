"""
Pattern-13: Increasing Number Triangle Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1
2 3
4 5 6

Input Format: N = 6
Result:   
1
2  3
4  5  6
7  8  9  10
11  12  13  14  15
16  17  18  19  20  21

"""

def Increasing_Number_Triangle_Pattern(N):
    pos = 0
    for indx in range(1, N + 1):
        for indx in range(1, indx + 1):
            pos += 1
            print(f"{pos} ", end='')
        print('')

N = int(input("Enter Positive Number:"))
Increasing_Number_Triangle_Pattern(N)