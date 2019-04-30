from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder


class AESDecryptor(object):
    """
    This encypts message using AES method.
    """

    def __init__(self, key):
        """
        constructor.

        Parameters
        ----------
        key: str
            This is the secret key.
            The `key` length must be 16 or 24 or 32.
        """

        if len(key)  in [16, 24, 32]:
            self.block_size = 16
            self.key = key.encode()
            self.unpad = (PKCS7Encoder()).decode
        else:
            raise TypeError('AESCryptor Error: Invalid length key!')

    def __str__(self):
        return f'<AESCryptor: block_size={self.block_size}>'

    __repr__ = __str__

    def encrypt(self, message, iv):
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(message)
        return encrypted

    def decrypt(self, encrypted, iv):
        """
        The AESEncryptor's instance decrypts `encrypted message`.

        Parameters
        ----------
        encrypted: bytes
            The encrypted message.
        iv: bytes
            The initialization vector.

        Returns
        -------
        message: bytes
            This is a message.
        """
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(encrypted)
        return decrypted


