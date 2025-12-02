# Caesar Cipher Tool

A simple Caesar Cipher implementation with a command-line interface for encrypting and decrypting messages.

## What is a Caesar Cipher?

The Caesar Cipher is a basic encryption algorithm where each letter in a message is shifted by a fixed number of places up/down the alphabet. For example, with a shift of 3, 'AB' becomes 'DE'.

## Installation/Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/SpencerS04/caesar_cipher_decryptor.git
    cd caesar_cipher_decryptor
   ```

2. Run the script using Python:

   ```bash
   PYTHONPATH=src python -m caesar_cipher.cli encrypt input.txt output.enc --shift 7
   ```

   ```bash
   PYTHONPATH=src python -m caesar_cipher.cli decrypt output.enc decrypted.txt --shift 7
   ```

## Project Structure

```text
src/
  caesar_cipher/
    __init__.py
    cipher.py      # core encrypt/decrypt logic
    cli.py         # command-line interface
tests/
  test_cipher.py   # basic roundtrip tests
README.md          # this file
```
