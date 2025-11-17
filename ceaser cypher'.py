alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',' ']
direction = input("Type 'encrypt' to encode , type 'decrypt' to decode : \n ").lower()
text = input("Type your message : \n").lower()
shift = int(input("Type the shift number: \n"))
def encrypt(original_text , shift_amount):
    ongoing = ""
    for letter in original_text :
        if letter in alphabet:
           enc_position =  alphabet.index(letter)+shift_amount
           enc_position %= len(alphabet)
           ongoing += alphabet[enc_position]
        if letter not in alphabet:
            ongoing += letter
    print(f"Here is the encoded text :\n{ongoing} ")

def decryption(original_text , shift_amount):
    ongoing = ""
    for letter in original_text :
        if letter in alphabet:
            enc_position = alphabet.index(letter) - shift_amount
            enc_position %= len(alphabet)
            ongoing += alphabet[enc_position]
        if letter not in alphabet:
            ongoing += letter
    print(f"Here is the decoded text :\n{ongoing} ")
if direction == "encrypt" :
    encrypt( original_text= text  , shift_amount= shift)
else:
    decryption( original_text = text , shift_amount= shift)