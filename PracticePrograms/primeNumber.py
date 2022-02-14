# logic - number is prime if its divisible by 1 and number itself
# run loop for 2 to num-1

print("Enter number:")
num = int(input())

for i in range(2,num-1):
    if (num%i == 0):
        print(f"{num} is not prime")
        break
else:
    print(f"{num} is prime")
    