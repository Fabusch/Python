# Eigene Funktion mit def Funktionsname():
                        #Methoden
                        
                        
                        
def my_func():
    print("Hello")
    print("this")
    print("is a Test")
    
    
my_func()



#Funktionen können Argumente (ARGUMENT)  übernehmen um den Output der Funktion zu generieren

def print_argument(word):
    print(word + "!")

print_argument("spam") 
print_argument("Hello")
print_argument("again")
#print_argument()  # Output Missin required Argument
#print_argument(1) # Error because 1 is an int and no String!  int can added with ! 

def print_int(int):   
    print(int + 1 )

print_int(2)



# Man kann wie so oft auch auch mehrere Parameter hinzufügen
def print_sum(x,y):
    print(x+y)
    
print_sum(2,10)

