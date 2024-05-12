"""
Pattern-6: Inverted Numbered Right Pyramid

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1 2 3
1 2
1 

Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1

"""

def Inverted_Numbered_Right_Pyramid(N):
    pattern = ""
    pattern_row = ""
    for indx in range(1, N + 1):
        pattern_row += f"{indx} "
        pattern = pattern_row + "\n" + pattern
    print(pattern)


N = int(input("Enter Positive Number:"))
Inverted_Numbered_Right_Pyramid(N)