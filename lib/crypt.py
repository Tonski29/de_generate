import gnupg

gpg = gnupg.GPG()

def aes_encrypt(data, passphrase):

    crypt = gpg.encrypt(data, encrypt=False,
                        symmetric= 'AES16',
                        passphrase=passphrase,
                        armor=True)

    print(data)
    print(crypt)
    return str(crypt)
