# numbers from 1 to N not divisible by 3 and 7

N = int(input("input N :"))

for num in range(1,N+1):
    if not((num % 3 == 0) and (num % 7 == 0)):
        print(num)
