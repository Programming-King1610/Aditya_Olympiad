# factorial of a number N

N = int(input("enter a number : "))
num = N                 # assign final result variable as num and initialize to N
while N != 1:           # loop until N decrases to 1 as multiplying by 1 is the same number so no need to have the last loop
    num = num * (N-1)   # factorial is N x N-1 x N-2 x N-3 .....
    N = N-1             # decrease value of N at end of each loop

print(num)
