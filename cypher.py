class Cypher:
    def __init__(self, key):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,;'
        self.key = key % len(self.alphabet)

    def encrypt(self, message):
        message = message.upper()
        encrypted_message = ''
        key_position = 0

        for letter in message:
            if letter in self.alphabet:
                new_letter_index = (self.alphabet.index(
                    letter) + self.key + key_position) % len(self.alphabet)
                key_position = (key_position + 1) % len(self.alphabet)
                encrypted_message += self.alphabet[new_letter_index]
            elif letter.isspace():
                encrypted_message += ' '
            else:
                raise ValueError(f'Unsupported character {letter}')

        return encrypted_message

    def decrypt(self, message, key=None):
        if key:
            self.key = key % len(self.alphabet)

        message = message.upper()
        decrypted_message = ''
        key_position = 0

        for letter in message:
            if letter in self.alphabet:
                new_letter_index = (self.alphabet.index(
                    letter) - self.key - key_position) % len(self.alphabet)
                key_position = (key_position + 1) % len(self.alphabet)

                if new_letter_index < 0:
                    new_letter_index += len(self.alphabet)

                decrypted_message += self.alphabet[new_letter_index]
            elif letter.isspace():
                decrypted_message += ' '
            else:
                if letter == 'Q':
                    key = int(input('Please enter the key: '))
                    self.key = key % len(self.alphabet)
                    print(f'Key set to {self.key}')
                else:
                    print(f'Unsupported character {letter}')

        return decrypted_message
