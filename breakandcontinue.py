#use break to stop a loop

from pickle import TRUE


i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("finished")


#Continue stops the current Iteration and continues to the next one

x = 0
while x<5:
    x +=1 # i = i+1
    if x == 3:
        print("Skipping 3")
        continue
    print(x)