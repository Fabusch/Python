#We can use a While Loop to repeat a block of code multiple times
#For Example we need to to procsess user inputs, so that each user input the same block of code need to execute

from re import X


i = 1
while i <=5:
    print(i)
    i = i +1
print("finished")


#The Code in the Body of a while Loop is executed repeatedly. this calles ITERATIOn

x = 3
while x >=0:
    print(i)
    i = i - 1
    
    
#If Else Statements are use for more Conditions
z = 1
while z < 10:
    if z%2 == 0:
        print(str(z) + "is even")   #str is used to convert the number of x to a string, so that it can be use for concatenation
    else:
        print(str(z) + "is odd")
        
z += 1


#Fill in the Blanks to create a loop that increments the value of x by 2 and print the even values

i = 1
while True:
    print(i)
    i += 1
    if(i > 5):
        break
# 1 2 3 4 5 

# but take care for infinite lopps that never stop automaticly< # example

a = 1
while a==1:
    print("hi this is a infiniy loop i never ending hehe")