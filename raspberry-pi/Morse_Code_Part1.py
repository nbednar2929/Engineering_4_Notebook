#type: ignore
#imports
import time 

#morse code library
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

while True: 
    #lowercases letters
    message = input("Your Message: ").upper()
    #defins message
    tmessage = ""
    #exits code if "-q" is tpyed
    if "-Q" in message:
        break
    #for loop with message
    for letter in range(len(message)):
        #converts letters to morse code
        tmessage += MORSE_CODE[message[letter]] + " "
    #prints message
    print(f"Your Translation: {tmessage}")
    time.sleep(1)