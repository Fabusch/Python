# The Else Statement can use then some Condition of the IF Statements is false

from re import X


x = 4 
if x == 5:
    print("Yes")
else:
    print("no")
    
    
    
if 1 + 1 == 2:   #true
    if 2 * 2 == 8: # false
        print("if") # so this is not true so the compiler goes to next Line
    else: # next line 
        print("else") # conclusion 


#Aber Achtung! Es kann immer nur ein Else Statement mit einem IF Statement verknüpft werden 
#Möchte man mehrer Dinge vergleichen geht dies so

num = 3
if num ==1:
    print("One")
else:
    if num == 2:
        print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("Something else")
            
            
#Another Example

x = 10
y = 20
if x > y:
    print("if statement")
else:
    print("else Statement")