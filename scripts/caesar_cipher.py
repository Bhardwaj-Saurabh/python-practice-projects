import string

class CeasarCipher:
    def __init__(self):
        self.alphabet_string = string.ascii_lowercase

    def get_user_input(self):
        self.user_input = input("Please Type Encode to encrypt or Decode to decrypt: ")
        self.user_message = input("Provide you message to Encode or Decode:\n")
        self.shift_no = int(input("Please Provide a number to shift: "))

    def encode_message(self):
        encoded_message = ''
        for letter in self.user_message: 
            if letter in self.alphabet_string:
                new_index = self.alphabet_string.index(letter) + self.shift_no
                print(new_index)

                if new_index >= len(self.alphabet_string):
                    new_index -= len(self.alphabet_string)
                encoded_message += self.alphabet_string[new_index]
            else:
                encoded_message += letter
        return encoded_message

    def decode_message(self):
        decoded_message = ''
        for letter in self.user_message: 
            if letter in self.alphabet_string:
                new_index = self.alphabet_string.index(letter) - self.shift_no
                decoded_message += self.alphabet_string[new_index]
            else:
                decoded_message += letter
        return decoded_message

    def encode_or_decode_message(self):
        self.get_user_input()
        if self.user_input.lower() == "encode":
            message = self.encode_message()
        elif self.user_input.lower() == "decode":
            message = self.decode_message()
        return message


if __name__ == "__main__":
    caeser_cipher = CeasarCipher()
    message = caeser_cipher.encode_or_decode_message()
    print(message)








