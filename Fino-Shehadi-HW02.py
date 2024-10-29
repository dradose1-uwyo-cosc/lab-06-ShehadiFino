# Shehadi Fino
# UWYO COSC 1010
# 10-28-24
# HW 02
# Lab Section:14
#Sources, people you worked with, help given to: Ryan
# your
# comments
# here

morse_code_dict = { 
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..'
}

def plaintext_to_morse_code(user_input):
    morse_code = ""
    for char in user_input:
        if char.isalpha():
            morse_code += morse_code_dict[char.upper()] + " "
        elif char == " ":
            morse_code += " "
    return morse_code.strip()

user_input = input("Enter a message to translate to Morse Code: ")
morse_code_output = plaintext_to_morse_code(user_input)
print("Morse Code:", morse_code_output)