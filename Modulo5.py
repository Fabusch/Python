list = [1,1,2,3,5,8,13]
print(list[list[4]])
# First Step list 4 is 5   and the Value of list 5 is 8   so the conclusion is 8 

# but never use list as a Variable Name is confused.



for i in range(10):
    if not i % 2 == 0:
        print (i +1)
        #Print all the even numbers between 2 and 10.



#iterate over the list using a loop and print the values

list = [1,2,3]
for var in list:
    print (var)
    
    
#output the first 3 charackters of a input string

x = input()
print(x[0:3])



y = [6,4,2,9]
y = y[::-1]               # Reverse the Array so it is 9,2,4,6
print(x[0]+x[2])            # the sum of the first and the third number 