alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(textx,shiftx,directionx):
    end_text=""
    if direction=="decode":
       shiftx*=-1   
    
    for letter in textx:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position+shiftx
            new_position%=26
            end_text+=alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {directionx}d result: {end_text}")    
from art import logo
print(logo)
should_end=False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caeser(textx=text,shiftx=shift,directionx=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
       should_end = True
       print("Goodbye")
         





#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.co/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛





#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.