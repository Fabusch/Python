def max(x,y):
    if x >=y:
        return x           
    else:
        return y

print(max(4,7))   # Outputs 7 because  y definited a the  2 argument is higher than the first argument declared as x 



def shortest_string(x, y):
    if len(x) < len(y): # len looks for the Shortest one. 
        return x
    else:
        return y

print(shortest_string("HELLO","HELLOOOW")) # Prints HELLO 



#Everything after the return statement will not be printed !

def add_numbers(x, y):
    total = x + y
    return total
    print("This wont be printed")   # <-- not printed bec after the return statement. 

print(add_numbers(4,5))

   

def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res



def func(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(func(4)) # 6 because res + i  means 0+0 = 0 , 0+1 = 1 , 0 + 2 = 2 , 0+3 = 3           1 + 2 + 3 = 6  it stops by iteration 3 because 4 is the stoppoint. 

        
    