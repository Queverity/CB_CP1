# CB 1st Caeser Cipher 


# main translator function
def translator(mode,text,key):
    # result string for translated characters to be put into
    result = ""
    # for loop so we can translate each and every character in a string
    for char in text:
        # checking if the character we are checking is an alphabetic character
        # if it is:
        if char.isalpha():
            # check what the mode the user entered is
            # if mode is Decode
            if mode == "Decode":
                # translate character into an ascii number using ord(), then shift it by subtracting the key
                shifted_letter = (ord(char) - key)
                # safety check to make sure that the ascii number does not goes past alphabetic characters, and instead loops through either uppercase or lowercase alphabet
                if char.isupper() and shifted_letter < 65:
                    shifted_letter += 26
                elif char.islower() and shifted_letter < 97:
                    shifted_letter += 26
                else:
                    # basically continues if the ascii number is within an acceptable range
                    pass
                # translates the ascii number back into a readable character
                shifted_letter = chr(shifted_letter)
                # appends shifted character to result string to be returned to user later
                result += shifted_letter
            elif mode == "Encode":
                # translate character into an ascii number using ord(), then shift it by subtracting the key
                shifted_letter = (ord(char) + key)
                # safety check to make sure that the ascii number does not goes past alphabetic characters, and instead loops through either uppercase or lowercase alphabet
                if char.isupper() and shifted_letter > 90:
                    shifted_letter -= 26
                elif char.islower() and shifted_letter > 122:
                    shifted_letter -= 26
                else:
                    # basically continues if the ascii number is within an acceptable range
                    pass
                # translates the ascii number back into a readable character
                shifted_letter = chr(shifted_letter)
                # appends shifted character to result string to be returned to user later
                result += shifted_letter
        # if character is not alphabetic, just add to result
        else:
            result += char
    # returning the result to be printed to the user
    return result


            


# telling the user what the program is
print("Caeser Cipher Decoder/Encoder")

# Main program loop
while True:
    #ask the user if they would like to decode or encode a piece of text, with a bit of stupid-proofing added on
    mode = input("Would you like to decode or encode a piece of text? Decode/Encode").strip().capitalize()
    # check if user input was decode
    if mode == "Decode":
        # ask for text to decode
        text = input("Enter text to decode: ").strip()
        # safety loop for making sure the user doesn't enter a key larger than 26 or smaller then -26
        while True:
            # ask for shift value/ cipher key
            key = int(input("Enter shift value").strip())
            # safety check
            if key > 26 or key < -26:
                print("invalid answer")
                continue
            else:
                break
            # call the function and enter arguments obtained from user to translate text using caeser cipher
        result = translator(mode,text,key)
        print(f"Decoded text:{result}")

    elif mode == "Encode":
        # ask for text to decode
        text = input("Enter text to decode: ").strip()
        # safety loop for making sure the user doesn't enter a key larger than 26 or smaller then -26
        while True:
            # ask for shift value/ cipher key
            key = int(input("Enter shift value").strip())
            # safety check
            if key > 26 or key < -26:
                print("invalid answer")
                continue
            else:
                break
            # call the function and enter arguments obtained from user to translate text using caeser cipher
        result = translator(mode,text,key)
        print(f"Encoded text:{result}")

    else:
        print("Invalid answer")
        continue

    # Ask the user if they want to continue
    go_again = input("Would you like to continue? Yes/No").strip().capitalize()
    # check if they said yes, if so continue, if not, then end the program.
    if go_again == "Yes":
        continue
    else:
        print("Goodbye!")
        break
    