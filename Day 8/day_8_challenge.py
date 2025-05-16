# Caesar Cipher
import art
from alphabet import alph as alphabet

print(art.logo)

def caesar(original_text, shift_amount, d):

        output_text = ""
        if d == "decode":
            shift_amount *= -1
        for letter in original_text:
            if letter not in alphabet:
                output_text += letter
            else:
                output_text += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
        print(f"Here is the {d}d message: {output_text}")

go_again = False

while not go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    redo = input("Type 'yes' if you want to go again. Otherwise type 'no'?\n")
    if redo == "no":
        go_again = True
        print("Goodbye!")



