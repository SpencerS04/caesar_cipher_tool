from caesar_cipher.cipher import encrypt, decrypt

def test_encrypt_decrypt_roundtrip():
    text = "Hello, World! 123"
    for shift in range(1, 26):
        enc = encrypt(text, shift)
        dec = decrypt(enc, shift)
        assert dec == text