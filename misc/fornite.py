import time
import sys

def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) 
    print() 
    
# --- Example Usage ---
typing_print("Hello, world! This text will appear as if it's being typed.")
typing_print("You can call this function multiple times for different messages.")
