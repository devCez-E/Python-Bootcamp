import alphabet
import art

should_continue = True
def caesar():
    if(direction == "encode"):
        encrypt(text, shift)
    else:
        decrypt(text, shift)
        
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet.alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.alphabet.index(letter)
        new_position = position - shift_amount
        cipher_text += alphabet.alphabet[new_position]
    print(f"The decoded text is {cipher_text}")

# -----------Main-----------

print(art.logo)

while(should_continue):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar()

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    should_continue = (result.lower() == 'yes')
    
print("Goodbye")

# -----------End-----------