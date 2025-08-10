def caesar_cipher(text: str, shifts: list[int], direction: int) -> str:
    """
    Encrypts or decrypts a text using the Caesar cipher with specified shifts.

    :param text: The input text to be encrypted or decrypted.
    :param shifts: A list of integers representing the shift values for each character.
    :param direction: 1 for encryption, -1 for decryption.
    :return: The transformed text after applying the Caesar cipher.
    """
    result = []
    shift_len = len(shifts)

    for i, char in enumerate(text):
        if char.isalpha():
            shift_amount = shifts[i % shift_len] * direction
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

#Function for encryption to plaintext.
def encrypt_caesar(plaintext: str, shifts: list[int],) -> str:
    return caesar_cipher(plaintext, shifts, 1)

#Function for decrypting the encrypted text.
def decrypt_caesar(ciphertext: str, shifts: list[int]) -> str:
    return caesar_cipher(ciphertext, shifts, -1)

test_plaintext = "Test text for Caesar cipher encryption and decryption."
test_shifts = [3, 1, 4]  # Example shifts for testing
test_ciphertext = encrypt_caesar(test_plaintext, test_shifts)
test_decrypted_text = decrypt_caesar(test_ciphertext, test_shifts)
# Test output
print(f"For example: \n")
print(f"Test plaintext: {test_plaintext}")
print(f"Test shifts: {test_shifts}")
print(f"Encrypted text: {test_ciphertext}")
print(f"Decrypted text: {test_decrypted_text}")


#User input for plaintext and number for shift/shifts.
user_plaintext = str(input('Enter a plaintext to encrypt: '))
user_shifts = list(map(int, input("Enter shift number/numbers: ").replace(",","").replace("-","").split()))

#To check if the user input is valid.
while True:
    user_shifts_input = input("Enter shift number/numbers (comma-separated): ")
    try:
        user_shifts = [int(i) for i in user_shifts_input.replace(",", " ").split()]
        if not user_shifts:
            print("Please enter at least one shift value.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter integers separated by commas or spaces.")

while True:
    user_plaintext = input("Enter plaintext to encrypt: ")
    if user_plaintext.strip():
        break
    else:
        print("Please enter a non-empty string for plaintext.")


#Encryption and decryption.
user_ciphertext = encrypt_caesar(user_plaintext, user_shifts)
decrypted_user_text = decrypt_caesar(user_ciphertext, user_shifts)

#Output
print(f"Original text: {user_plaintext}")
print(f"Encrypted text: {user_ciphertext}")
print(f"Decrypted text: {decrypted_user_text}")