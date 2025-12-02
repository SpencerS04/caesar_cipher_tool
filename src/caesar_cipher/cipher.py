#!/usr/bin/env python3

def encrypt(text: str, shift: int) -> str:
    result_chars = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result_chars.append(chr(shifted))
        else:
            result_chars.append(char)
    return "".join(result_chars)

def decrypt(text: str, shift: int) -> str:
    return encrypt(text, 26 - shift)

def auto_freq_decrypt(text:str, newFile):
    # TODO - add frequency analysis decryptor
    pass
