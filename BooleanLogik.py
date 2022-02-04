#Boolean Operators can check with alot of  Operators
# mit der and and / und Verbindung
print (1 == 1 and 2 == 2 ) #true

print (1 == 1 and 2 == 3 ) #False

# Der OR Operator ist True wenn eine(oder beide) True sind    und False wenn beide Bedingungen false sind


print ( 1 == 1 or 2 == 3) #True

print (2 < 1 or 3 > 6 ) #false 


#The NOT Operator say its false if the normaly conclusion is true und umgekehrt

print(not 1 == 1 ) # False
print(not 1 > 7 ) #True 


if not True:
    print("1")
elif not (1+1 ==3):
    print("2")
else:
    print("3")
    #Conclcusion is 2  because 1+1(2) is not equal to 3. 