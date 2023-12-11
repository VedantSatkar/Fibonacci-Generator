#Task 1


#FIBONACCI SERIES GENERATOR


#Fibonacci Generator Series of Sum of Two Numbers.

num = int(input("Enter any number user want :"))

n1 = 0
n2 = 1
#n3 = 0
sum =0

if num<=0:
        print('Please Enter number greather than 0')

else:
    for i in range(0, num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2

#while sum<=num:
 #   print(n3)
  #  n1 = n2
   # n2 = n3
    #n3 = n1+n2
