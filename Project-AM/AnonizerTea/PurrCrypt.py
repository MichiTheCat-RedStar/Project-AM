# Данный код распространяется по MIT лицензии автром MichiTheCat
# Не видитесь на проекты, выдающие себя за оригинал или подобное
# Оригинал кода https://github.com/MichiTheCat-RedStar/PurrCrypt


from random import seed, getrandbits

def purr_encode(*text:str) -> str:
    "Позволяет превращать текст в Purr"
    text = ' '.join(text)
    value = str(text).encode('utf-8')
    value = int.from_bytes(value, byteorder='big')
    value = bin(value)[2:]
    result = 'Pu'
    for num in value:
        if num == '1': result += 'R'
        else: result += 'r'
    return result


def purr_decode(text:str) -> str:
    "Позволяет превращать Purr в текст"
    if text[0:2] != 'Pu':
        raise ValueError("Строка должна начинаться с 'Pu'")
    result = text[2:]
    value = ''
    for sym in result:
        if sym == 'R': value += '1'
        elif sym == 'r': value += '0'
        else: raise ValueError('Недопустимый символ')
    byte_len = (len(result) + 7) // 8
    result = int(value, 2).to_bytes(byte_len, 'big')
    return result.decode('utf-8')


def purr_encrypt(*text:str, key=42) -> str:
    "Позволяет превращать текст в Purr используя key"
    seed(key)
    text = ' '.join(text)
    value = str(text).encode('utf-8')
    value = int.from_bytes(value, byteorder='big')
    value = bin(value)[2:]
    result = 'Pu'
    for num in value:
        if num == '1':
            if getrandbits(1):
                result += 'R'
            else:
                result += 'r'
        else:
            if getrandbits(1):
                result += 'r'
            else:
                result += 'R'
    seed(None)
    return result


def purr_decrypt(text:str, key=42) -> str:
    "Позволяет превращать Purr в текст используя key"
    seed(key)
    if text[0:2] != 'Pu':
        raise ValueError("Строка должна начинаться с 'Pu'")
    result = text[2:]
    value = ''
    for sym in result:
        if sym == 'R':
            if getrandbits(1):
                value += '1'
            else:
                value += '0'
        elif sym == 'r':
            if getrandbits(1):
                value += '0'
            else:
                value += '1'
        else:
            raise ValueError('Недопустимый символ')
    seed(None)
    byte_len = (len(result) + 7) // 8
    result = int(value, 2).to_bytes(byte_len, 'big')
    return result.decode('utf-8')


if __name__ == '__main__':
    
    TEXT = 'Meowdy PurrCrypt!'
    print('Было:', TEXT)

    TEXT = purr_encrypt(TEXT, key=8)
    print('Закодировали:', TEXT)

    TEXT = purr_decrypt(TEXT, key=8)
    print('Выкодировали:', TEXT)