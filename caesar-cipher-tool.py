def encrypt_ceaser(plaintext, shifts):      #Function for encryption to plaintext.
    ciphertext = ""
    shift_len = len(shifts)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift_amount = shifts[i % shift_len]    #To give an option for multiple shifts.
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            ciphertext += new_char
        else:
            ciphertext += char

    return ciphertext

def decrypt_caesar(ciphertext, shifts):     #Function for decrypting the encrypted text.
    plaintext = ""
    shift_len = len(shifts)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift_amount = shifts[i % shift_len]    #To give an option for multiple shifts.
            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            plaintext += new_char
        else:
            plaintext += char
    return plaintext

#User input for plaintext and number for shift/shifts.
user_plaintext = str(input('Enter a plaintext to encrypt: '))
user_shifts = list(map(int, input("Enter shift number/numbers: ").replace(",","").split()))

#Encryption and decryption.
user_ciphertext = encrypt_ceaser(user_plaintext, user_shifts)
decrypted_user_text = decrypt_caesar(user_ciphertext, user_shifts)

#Output
print(f"Original text: {user_plaintext}")
print(f"Encrypted text: {user_ciphertext}")
print(f"Decrypted text: {decrypted_user_text}")