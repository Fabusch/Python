# How many Times execute the Statement

while False:
    print("looping") # No times because the Statement is false.
    
# break the infitinite loop when the user enters '0'

while True:
    x = input()
    if x == '0':
        break


# Take Number from Input and Output "Pass" if its greater than 70

grade = int(input())
if grade > 70:
    print("Pass")
    
    
    
    
i = 0
x = 0
while i < 4:
    x+=i
    i+=1

print(x) #6 x =0 , i =0 while i<4 x+ = i ,
#i+ = 1 1st loop x = 0 + 0 = 0 i = 0 + 1 = 1 
# 2nd loop x = 0 + 1 = 1 i = 1 + 1 = 2 
# 3rd loop x = 1 + 2 = 3 i = 2 + 1 = 3 
# 4th loop x = 3 + 3 = 6 i = 3 + 1 = 4( i not less than 4 and program stop here ) So, the value of x is 6.