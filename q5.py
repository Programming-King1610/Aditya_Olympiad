#Declare lowerBound:integer
#Declare upperBound:integer
#Declare num:integer


primeSum = 0        # initialise variable to calculate sum of prime numbers
lowerBound = int(input("Enter lower bound: "))
upperBound = int(input("Enter upper bound: "))

for N in range(lowerBound, upperBound + 1): # N variable gets a new number in each iteration
    counter = 0                             # set counter to 0 for each loop
    for num in range(1,N + 1):               # second nested loop with num variable looping from 1 to N
        if N % num == 0:                        # testing if num is a factor of N
            counter = counter + 1                # counting the no. of factors of N
    if counter == 2:
        print(N)                            # print out the value of prime number
        primeSum = primeSum + N                 # taking sum of the prime numbers in each loop


print('sum of the prime numbers: ' + str(primeSum))