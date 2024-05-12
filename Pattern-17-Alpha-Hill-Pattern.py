"""
Pattern-17: Alpha-Hill Pattern

Problem Statement: Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
  A  
 ABA 
ABCBA


Input Format: N = 6
Result:   
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA

"""

def Alpha_Hill_Pattern(N):
    letter = 64
    pattern = ''
    for indx in range(1,N+1):
        pattern += chr(letter + indx)
        print((" " * (N - indx)) + pattern + pattern[:-1][::-1])

N = int(input("Enter Positive Number:"))
Alpha_Hill_Pattern(N)