from cypher import Cypher


def main():
    raw = input('Enter Text: ')
    key = int(input('Enter Key: '))

    cypher = Cypher(key)

    encrypted = cypher.encrypt(raw)
    print(encrypted)

    print(cypher.decrypt(encrypted, key))


main()
