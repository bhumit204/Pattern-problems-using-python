"""
Pattern-4: Right-Angled Number Pyramid - II

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1
2 2 
3 3 3

Input Format: N = 6
Result:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

"""

def Right_Angled_Number_Pyramid2(N):
    for indx in range(1, N + 1):
        print(f"{indx} " * indx)


N = int(input("Enter Positive Number:"))
Right_Angled_Number_Pyramid2(N)