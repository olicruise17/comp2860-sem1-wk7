# Name: Oliver Cruise
# StudentID: 201823825

class VigenereCipher:
    """
       VigenereCipher class (TO BE COMPLETED).

       Attributes:
           keyword (str): The word to be used as the key
           offset (int): The ASCII value of the letter 'A'. A static utility attribute to help you calculate
                a letter's position in the alphabet from 0 (A) to 25 (Z).
    """
    offset = ord('A')

    # constructor class, sets keyword

    def __init__(self, keyword: str):
        self.keyword = keyword.upper()

    # shift letter method, shifts letter forward or backward

    def __shift_letter(self, letter: str, shift: int, forward: bool):

        # finds position

        position = ord(letter) - VigenereCipher.offset

        # shifts letter forward or backward

        if forward:
            new_position = (position + shift) % 26
        else:
            new_position = (position - shift) % 26

        # converts new position back to letter

        shifted_letter = chr(new_position + VigenereCipher.offset)
        return shifted_letter

    # generates shift list method, generates list of shifts for each letter in plaintext

    def __generate_shift_list(self, plaintext_length: int):

        words = []
        shift_list = []

        # finds lenght of keyword and how many times it needs to be repeated

        length_keyword = len(self.keyword)
        whole = plaintext_length // length_keyword
        remainder = plaintext_length % length_keyword

        for i in range(whole):
            words.append(self.keyword)

        words.append(self.keyword[:remainder])
        shift_string = "".join(words)

        # converts each letter in shift_string to its position in the alphabet and appends to shift_list

        for char in shift_string:
            position = ord(char) - VigenereCipher.offset
            shift_list.append(position)

        return shift_list

    # encrypt method, encrypts plaintext string

    def encrypt(self, plaintext: str):

        # converts to uppercase

        ciphertext = ''
        upper_text = plaintext.upper()
        new_text = ""

        # removes whitespace and punctuation from the input

        for char in upper_text:
            if char.isalpha():
                new_text += char

        # creates the list of shifts for each letter in the plaintext

        shifted_list = self.__generate_shift_list(len(new_text))

        current = 0

        # uses self.__shift_letter to encrypt an individual letter

        for char in new_text:
            shifted_letter = self.__shift_letter(char, shifted_list[current], True)
            ciphertext += shifted_letter
            current += 1

        return ciphertext

    # decrypt method, decrypts ciphertext string
    
    def decrypt(self, ciphertext: str):

        upper_text = ciphertext.upper()
        new_text = ""

        for char in upper_text:
            if char.isalpha():
                new_text += char

        shifted_list = self.__generate_shift_list(len(new_text))

        plaintext = ''
        current = 0

        # uses self.__shift_letter to decrypt an individual letter

        for char in new_text:
            shifted_letter = self.__shift_letter(char, shifted_list[current], False)
            plaintext += shifted_letter
            current += 1

        return plaintext


def main():
    vig_cipher = VigenereCipher('smarties')
    ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
    plaintext = vig_cipher.decrypt(ciphertext)
    print(plaintext)
    assert plaintext == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'


if __name__ == "__main__":
    main()