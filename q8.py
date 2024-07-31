# pick largest number from a list of numbers on the console


largestNum = 0                              # initialize the largest number variable to something really small
smallestNum = 10000000000000000000000000    # initialize the smallest number variable to something really big
num = (input("Input number or press enter to stop : "))
if num == "":
    print("No numbers entered")
while num != "":
    if int(num) > int(largestNum):
        largestNum = num
    elif int(num) < int(smallestNum):
        smallestNum = num
    num = (input("Input number or press enter to stop : "))


    print("smallest number : "+ str(smallestNum))
    print("largest number : "+ str(largestNum))