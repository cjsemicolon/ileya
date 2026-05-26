#create a function that collects password and the shift
#initialize a variable to collect the encrypted password
#loop through password to verify if a character is an alphabet
#convert the letter to its ascii value
#shift the ascii value by shift amount
#if you run out of alphabets start from the begining
#convert shifted ascii value back to alphabet
#add shifted alphabet to the encrypted password variable

def encryption(password, shift):
    encrypted_password = ""
    for character in password:
        if character.isalpha():
            if character.islower():
                first_letter = ord("a")
            else:
                first_letter = ord("A")

            position = ord(character) - first_letter
            
            new_position = (position + shift) % 26
            
            encrypted_character = chr(new_position + first_letter)        
                
            encrypted_password += encrypted_character
        
        else:
            
            encrypted_password += character

    return encrypted_password
