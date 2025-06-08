from Day8_CaesarCipherAlphabet import alphabet
from Day8_CaesarCipherArt import logo

print(logo)


def encrypt(text, shift):
    text = text.lower()
    encrypted_message = ""
    for i in range(len(text)):
        # print(alphabet.__getitem__(alphabet.index(text[i]) + shift))
        if text[i] not in alphabet:
            encrypted_message += text[i]
        else:
            encrypted_message += alphabet.__getitem__((alphabet.index(text[i]) + shift) % len(alphabet))
    print(f"Here is the Encrypted message : {encrypted_message}")


def decrypt(text, shift):
    text = text.lower()
    decrypted_message = ""
    for i in range(len(text)):
        # print(alphabet.__getitem__(alphabet.index(text[i]) - shift))
        if text[i] not in alphabet:
            decrypted_message += text[i]
        else:
            decrypted_message += alphabet.__getitem__((alphabet.index(text[i]) - shift) % len(alphabet))
    print(f"Here is the original message : {decrypted_message}")


def caesar(option_chosen):
    while option_chosen:
        direction = input("Enter 'E' for Encrypt; Enter 'D' for Decrypt : ")

        match direction:
            case "E":
                text = input("Enter your message : ").upper()
                shift = int(input("Enter the shift amount: "))
                encrypt(text, shift)
            case "D":
                text = input("Enter your message : ").upper()
                shift = int(input("Enter the shift amount: "))
                decrypt(text, shift)
            case default:
                print("Choose a valid option in between 'E' or 'D' :<")
        take_option = input("Do you want to go again? 'Y' for 'Yes' & 'N' for 'NO' : ")
        option_chosen = True if take_option == "Y" else False
    print("Thanks for using it! :)")


option = True
caesar(option)
