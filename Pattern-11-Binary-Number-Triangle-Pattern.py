"""
Pattern-11: Binary Number Triangle Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1
01
101

Input Format: N = 6
Result:   
1
01
101
0101
10101
010101

"""

def Binary_Number_Triangle_Pattern(N):
    for indx in range(1, N + 1):
        pos = indx % 2
        for indx2 in range(1,indx+1):
            print(pos, end='')
            pos = 1 - pos
        print('')

N = int(input("Enter Positive nunber:"))
Binary_Number_Triangle_Pattern(N)