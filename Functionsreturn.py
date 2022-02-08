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