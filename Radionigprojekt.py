# SPLIT  Strings by Space Example
msg  = str(input())
splitText = msg.split()
print(splitText)
scores = { 
    "A": 1,
    "I": 1,
    "J": 1,
    "Q": 1,
    "Y": 1,
    "B": 2,
    "K": 2,
    "R": 2,
    "C": 3,
    "G": 3,
    "L": 2,
    "S": 2,
    "D": 4,
    "M": 4,
    "T": 4,
    "E": 5,
    "H": 5,
    "N": 5,
    "X": 5,
    "U": 6,
    "V": 6,
    "W": 6,
    "O": 7,
    "Z": 7,
    "F": 8,
    "P": 8
}
score = 0



for char in splitText:    # in msg works
    score += scores[char]       

x = score
print(x)


# HELLO in 21 umwandeln funktioniert  Hello World in eine Liste umwandeln klappt auch .   Einzelne Listenwörter in den Zahlen des Scores umwandeln klappt noch nicht. 