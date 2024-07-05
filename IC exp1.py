def caesar_cipher(text, shift, encrypt=True):
    """
    Encrypt or decrypt a given text using Caesar Cipher.

    Args:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The shift value for the Caesar Cipher.
        encrypt (bool, optional): Encrypt if True, decrypt if False. Defaults to True.

    Returns:
        str: The resulting text after encryption or decryption.
    """
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            base = ord('A') if char.isupper() else ord('a')
            shift_direction = shift if encrypt else -shift
            result += chr((ord(char) - base + shift_direction) % 26 + base)
        else:
            result += char
    return result

def get_user_choice():
    """
    Prompt the user to choose between encryption and decryption.

    Returns:
        str: 'e' for encryption or 'd' for decryption.
    """
    while True:
        choice = input("Choose Encryption (e) or Decryption (d): ").strip().lower()
        if choice in ('e', 'd'):
            return choice
        else:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

def get_shift_value():
    """
    Prompt the user to enter a valid shift value.

    Returns:
        int: A valid shift value between 0 and 25.
    """
    while True:
        try:
            shift = int(input("Enter the shift value (0-25): ").strip())
            if 0 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 0 and 25.")
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 25.")

def main():
    """
    The main function that handles user input and performs the Caesar Cipher operation.
    """
    while True:
        choice = get_user_choice()
        text = input("Enter the text: ").strip()
        shift = get_shift_value()

        if choice == "e":
            result = caesar_cipher(text, shift, encrypt=True)
            print("The cipher text is:", result)
        else:
            result = caesar_cipher(text, shift, encrypt=False)
            print("The plain text is:", result)

        retry = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if retry not in ('yes', 'y'):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
