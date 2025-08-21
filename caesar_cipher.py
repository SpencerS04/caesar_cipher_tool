#!/usr/bin/env python3
import random

def main():
    fileName = input("File name: ")
    
    with open(fileName, "rt") as f:
        fileContent = f.read()
    
    shiftKey = random.randint(1,25)
    print("The shift value is " + str(shiftKey))
    
    with open("encrypt_"+fileName, "wt") as f:
        for char in fileContent:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shiftKey) % 26 + base
                f.write(chr(shifted))
            else:
                f.write(char)

if __name__ == "__main__":
    main()