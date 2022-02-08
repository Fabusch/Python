#to create number sequenze use the range() function

#by default, it starts from 0, increment by 1 and stops BEFORE the specific number

numbers = list(range(10))   #rangefunction creates a sequence of integers.
print(numbers)


nums = list(range(5))
print(nums[4])


#But u dont must put Range in a list
print(range(5)[4]) # gives the Same output and u dont got an List.

# If rankes startet with no argument they starts from 0 - the first argument like range(10)
#but if u startet with two arguments they startet from th first to the second
print(range(2,4))   #  2,3 

print(range(20 == list)(range(0,20))) #true   # all goes from 0 - 19 

# U can add three Elements the third Argument called STEP

third = list(range(5,20,2))
print(third)  # 5,7,9,11,13,15,17,19


#For Loops in Range

for i in range(5):
    print("Hello")   # So u get 6 Times Hello 0 , 1 , 2 ,3 ,4,5 ranges 
    
    

#Create a Loop that prints only even values in the range

for x in range (0,20,2):
    print(x)