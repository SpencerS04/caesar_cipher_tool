#!/usr/bin/env python3
import random

def main():
    fileName = input("File name: ")
    
    with open(fileName, "rt") as f:
        fileContent = f.read()
    
    shiftKey = random.randint(1,25)
    print("The shift value is " + str(shiftKey))
    
    with open("encrypt_"+fileName, "wt") as f:
        encrypt(fileContent, shiftKey, f)
    with open("decrypt_"+fileName, "wt") as f:
        encrypt(fileContent, shiftKey, f)


def encrypt(text: str, shift: int, newFile):
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            newFile.write(chr(shifted))
        else:
            newFile.write(char)

def decrypt(text: str, shift: int, newFile):
    shift = 26-shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            newFile.write(chr(shifted))
        else:
            newFile.write(char)

def auto_freq_decrypt(text:str, newFile):
    # TODO - add frequency analysis decryptor
    pass


if __name__ == "__main__":
    main()