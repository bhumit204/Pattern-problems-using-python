"""
Pattern-3: Right-Angled Number Pyramid

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1
1 2 
1 2 3

Input Format: N = 6
Result:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

"""

def Right_Angled_Number_Pyramid(N):
    pattern_row = ""
    for indx in range(1, N + 1):
        pattern_row += f"{indx} "
        print(pattern_row)


N = int(input("Enter Positive Number:"))
Right_Angled_Number_Pyramid(N)