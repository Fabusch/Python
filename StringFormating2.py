# join - verbindet eine Liste von String mit einem anderen String als Trennzeichen und gibt einen String zurück

print(",".join(["spam","eggs","ham"]))  # The Commata will included in the spam eggs ham string 
# prints "spam,eggs,ham" # no List!

# Replace   ersetzt das ausgewählte Wort im String mit dem Argument
print("HELLO ME".replace("ME","TEST")) # Prints HELLO TEST

#startswith / endswith       determine True of False is a String startet/endet with the Selectet Word
print(("HELLO AGE").startswith("HELLO"))
print(("HELLO END").endwith("END")) # True

#Lower and Upper chance the cases of a string
print(("Hello").upper())
print(("HeLlO ChANGE").lower())

#split  ist das Gegenteil von Join aus einem String wird eine Liste mit dem Argument als Trennzeichen
print("spam,eggs,ham".split(", "))
#prints "['spam', 'eggs', 'ham]"
