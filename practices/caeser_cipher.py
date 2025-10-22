# CB 1st Caeser Cipher 

def translator(mode,text,key):
    result = ""
    for char in text:
        if char.isalpha():
            if mode == "Decode":
                shifted_letter = (ord(char) - key)
                if char.isupper() and shifted_letter < 90:
                    shifted_letter -= 26
                elif char.islower() and shifted_letter < 122:
                    shifted_letter -= 26
                else:
                    pass
                shifted_letter = chr(shifted_letter)
                result += shifted_letter
            elif mode == "Encode":
                shifted_letter = (ord(char) + key)
                if char.isupper() and shifted_letter > 65:
                    shifted_letter += 26
                elif char.islower() and shifted_letter > 97:
                    shifted_letter += 26
                shifted_letter = chr(shifted_letter)
                result += shifted_letter
        else:
            result += char
    return result

            



print("Caeser Cipher Decoder/Encoder")

while True:
    mode = input("Would you like to decode or encode a piece of text?").strip().capitalize()
    if mode == "Decode":
        text = input("Enter text to decode: ").strip()
        e = int(input("Enter shift value").strip())
        result = translator(mode,text,key)
        print(f"Decoded text:{result}")

    elif mode == "Encode":
        text = input("Enter text to encode: ").strip()
        key = int(input("Enter shift value: ").strip())
        result = translator(mode,text,key)
        print(f"Encoded text:{result}")
    else:
        print("Invalid answer")
        continue
    go_again = input("Would you like to continue? Yes/No").strip().capitalize()
    if go_again == "Yes":
        continue
    else:
        print("Goodbye!")
        break
    