# TO generate a new List from antoher list u can use slices 


squares = [0,1,4,9,16,25,36,49,64,81]

print(squares[2:6])   # 4,9,16,25
print(squares[3:8])  # 9, 16, 25, 36, 49
print(squares[0:1]) # 0

# lst[Initial:END:IndexJump]

 # squares is a list from 0 - 10 
 # if u :   squars the List will b  cuted with the arguments
 
print(squares[1:5])  #  1 , 4 , 9 , 16   




sqs = [0,1,4,9,16,25,36,49,64,81]
print(sqs[1::4]) # Starts with 1 goes 4 steps all time so  1 , 25 ,81 

# its possible to do it negative 

sqs1 = [0,1,4,9,16,25,36,49,64,81]
print(sqs1[7::5-1]) # [49,36]
