num = [4, 5, 6]

msg = "Number: {0} {1} {2}".format(num[0], num[1], num[2])
print(msg)
print("\n \n")
num = [1, 2, 3, 4, 5, 6]
msg = "Number: {0} {1} {2}".format(num[1], num[0], num[1])
print(msg)
print("\n \n")
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
msg = "Number: {0} {1} {2}".format(num[3], num[0], num[8])
print(msg)
print("\n \n")
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# so its well know that num[0] = 1 and so on....


print("{0}{4}{2}{5}{4}{6}{1}{8}{7}{8}{3}".format("An", "na", "k", "coding", "s", "ri", "h", "is", " "))
print("\n \n")


check = ("funny, right?")
ch = "---".join(check)
print(ch)
print("\n \n")
ch = ch.replace(",", "###")
ch = ch.replace("---", "  ")
print(ch)
print("\n \n")
ch = ch.upper()
print(ch)
print("\n \n")
ch = ch.replace("###", ",")
ch = ch.lower()
print(ch)

print("{0}{1}{0}".format("abra","cad"))
# We can also name placeholders, instead of an index nr
a = "{x},{y}".format(x=5,y=12)
print(a)

str="{c},{b},{a}".format(a=5,b=9,c=7)  
print(str) #7,9,5