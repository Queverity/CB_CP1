# CB 1st Caeser Cipher 

def encode(text,shift_value):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("a") if char.islower() else ord("A")
            shifted_letter = 

            

def decode(text,shift_value):
    

print("Caeser Cipher Decoder/Encoder")

while True:
    task = input("Would you like to decode or encode a piece of text?").strip().capitalize()
    if task == "Decode":
        text = input("Enter text to decode: ").strip()
        shift_value = int(input("Enter shift value").strip())
        print(f"Decoded text:{decode(text,shift_value)}")

    elif task == "Encode":
        text = input("Enter text to encode: ").strip()
        shift_value = int(input("Enter shift value").strip())
        print(f"Encoded text:{encode(text,shift_value)}")
    else:
        print("Invalid answer")
        continue
    go_again = input("Would you like to continue? Yes/No").strip().capitalize()
    