alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# region TODO list

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

# TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
# print output: "The decoded text is hello"


# TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# TODO-7: Combine the encrypt() and decrypt() functions into a single function called caesar().

# TODO-8: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# endregion

# region making encrypt function
# TODO-1
# def encrypt(text: str, shift: int):
#     result = ""
#     # TODO-2
#     for char in text:
#         char_index = alphabet.index(char)
#         if char_index + shift >= 25:
#             char_index = (char_index + shift) - len(alphabet)
#             result += alphabet[char_index]
#         else:
#             result += alphabet[char_index + shift]
#     print(f"The encoded text is {result}")

# TODO-3
# encrypt(text=text, shift=shift)

# endregion

# region making decrypt function
# TODO-4
# def decrypt(text: str, shift: int):
#     result = ""
#     # TODO-5
#     for char in text:
#         char_index = alphabet.index(char)
#         result += alphabet[char_index - shift]
#     print(f"The decoded text is {result}")


# endregion

# region calling individual functions

# TODO-6
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)

# endregion

# TODO-7
def caesar(text: str, shift: int, direction: str):
    result = ""
    for char in text:
        char_index = alphabet.index(char)
        if direction == "encode":
            if char_index + shift >= 25:
                char_index = (char_index + shift) - len(alphabet)
                result += alphabet[char_index]
            else:
                result += alphabet[char_index + shift]
        elif direction == 'decode':
            result += alphabet[char_index - shift]

    print(f"The {direction}d text is {result}")

# TODO-8
caesar(text, shift, direction)
