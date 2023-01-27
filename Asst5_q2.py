lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
num = int(input("Enter the number: "))

# use loop to iterate over the range
for i in range(lower,upper + 1):
    if(i % num == 0):
        print(i)