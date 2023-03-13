#author: Grieger, Adrian
#version: 1.0.1
#last updated: 25.02.23
#
#
#
#
#
#     -made some efficiency upgrades
#     -fixed a bug where your code wouldn't get translated correctly or the program would've crashed
#  v.1.0.1
#     -changed whole encrypting system to be much more secure and efficient than before.
#     -minor design changes
#  v.1.0.0

import os

# This function takes a character as an argument and returns the corresponding encrypted character
# a --> z
# z --> a
# b --> y
# y --> b
def charChar(char):
    distanceToStart = ord(char)
    return chr(126 - distanceToStart)

# This function takes a message as an argument and returns the encrypted message
def encryptMessage(message):
    encryptedMessage = ""
    for i in range(len(message)):
        originalChar = message[i]
        # Use charChar() to encrypt the current character
        encryptedIndex = ord((charChar(originalChar)))
        encryptedChar = chr(encryptedIndex)
        encryptedMessage += encryptedChar
    return encryptedMessage

# Loop indefinitely to allow the user to encrypt and decrypt multiple messages
while True:
    asciiMultipliedMessage = ""
    multiplier = 1
    # Prompt the user for a code word, which is used to generate a multiplier
    multiplierWord = input("Code: ")
    for i in range(0, len(multiplierWord)):
        # Multiply the ASCII values of each character in the code word to generate a multiplier
        multiplier *= ord(multiplierWord[i])
    # Prompt the user to select "e" for encrypting or "d" for decrypting
    encryptDecrypt = input("e for encrypting and d for decrypting: ")
    if encryptDecrypt == "e": # Encrypting
        # Prompt the user for a message to encrypt
        message = input("Enter your decrypted message: ")
        # Use encryptMessage() to encrypt the message
        switchedMessage = encryptMessage(message)
        # Multiply the ASCII value of each encrypted character by the multiplier and concatenate the results
        for i in range(0, len(switchedMessage)):
            asciiMultipliedMessage += str(ord(switchedMessage[i]) * multiplier) + "-"
        answer = asciiMultipliedMessage[:-1]
        # Copy the encrypted message to the clipboard and display it
        command = 'echo ' + answer.strip() + '| clip'
        os.system(command)
        print(answer)
    elif encryptDecrypt == "d": # Decrypting
        # Prompt the user for an encrypted message
        message = input("Enter your encrypted message: ").split("-")
        for i in range(0, len(message)):
            # Divide each ASCII value by the multiplier to reverse the multiplication process
            message[i] = int(message[i])
        switchedMessage = ""
        # Convert the resulting ASCII values to characters using encryptMessage()
        for i in range(0, len(message)):
            switchedMessage += chr(int(message[i] / multiplier))
        # Use encryptMessage() to decrypt the switched message
        answer = encryptMessage(switchedMessage)
        # Copy the decrypted message to the clipboard and display it
        command = 'echo ' + answer.strip() + '| clip'
        os.system(command)
        print(answer)
    # Wait for the user to press enter before clearing the screen
    input("Press enter to clear screen...")
    os.system('cls||clear') # Clear the screen