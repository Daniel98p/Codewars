def encrypter(string):
    return maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')


if __name__ == '__main__':
    from string import maketrans
    encrypter('nbc')


