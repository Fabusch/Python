words = ["hello","world","spam","eggs"]

for word in words: #Die Word Variable ist das entsprechende Element in der Liste 
    print(word + "!")          
    
    
    
letter = ['a','b','c']
for l in letter: # Hier is L die Variable die generiert wird 
    print(l)
    
    
    
# A for Loop can be used to iterate over Strings

str = "testing loops"
count = 0

for x in str:
    if( x == 't'):
        count += 1
print(count) #  2 because t is 2 times in str 




list = [2,3,4,5,6,7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break
    
    
# For vs While
# For schleife wenn die Anzahl der Iterationen festgelegt ist 
# While Schleife wenn die Iteraktionen nicht bekannt ist und von den Bedingungen abhängig ist. 