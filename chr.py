 ''' Prints ASCII characters''' 
numbers = list(range(1,10000))
  
for number in numbers:
      
    # Convert ASCII-based number to character.
    letter = chr(number)
    print("Character of ASCII value", number, "is ", letter)