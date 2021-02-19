def split(word):
    return [char for char in word]


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = split(alphabet)


def encrypt_text_by_keyword(text, keyword):
    keyword_list = split(keyword)
    encryption_list = []
    for character in keyword_list:
        if character not in encryption_list:
            encryption_list.append(character)

    for character in alphabet_list:
        if character not in encryption_list:
            encryption_list.append(character)
    print(encryption_list)
    encrypted_text = ''
    for character in text:
        encrypted_character = character
        if character in alphabet_list:
            encrypted_character = encryption_list[alphabet_list.index(character)]
        elif character.lower() in alphabet_list:
            encrypted_character = encryption_list[alphabet_list.index(character.lower())].upper()

        encrypted_text += encrypted_character

    return encrypted_text


def decrypt_text_by_keyword(text, keyword):
    keyword_list = split(keyword)
    encryption_list = []
    for character in keyword_list:
        if character not in encryption_list:
            encryption_list.append(character)

    for character in alphabet_list:
        if character not in encryption_list:
            encryption_list.append(character)

    decrypted_text = ''
    for character in text:
        encrypted_character = character
        if character in encryption_list:
            encrypted_character = alphabet_list[encryption_list.index(character)]
        elif character.lower() in encryption_list:
            encrypted_character = alphabet_list[encryption_list.index(character.lower())].upper()

        decrypted_text += encrypted_character

    return decrypted_text


if __name__ == '__main__':
    print(
        encrypt_text_by_keyword(
            text="This is a sample line to encrypt.",
            keyword='rocketships',
        )
    )

    print(
        decrypt_text_by_keyword(
            text="Qhin in r nrdjbe bife qg efcmyjq.",
            keyword='rocketships',
        )
    )
