import random, string

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def random_token(n=16):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))


class AESCryptor(object):
    """
    This encypts message using AES method.
    """

    def __init__(self, key, encoded=False):
        """
        constructor.

        Parameters
        ----------
        key: str
            This is the secret key.
            The `key` length must be 16 or 24 or 32.
        encoded: bool
            Is the `key` encoded? True or False?
        """

        if len(key) not in [16, 24, 32]:
            raise TypeError('Invalid length key!')
        else:
            self.block_size = len(key)
            self.key = key if encoded else key.encode()

    def __str__(self):
        return f'<AESCryptor: block_size={self.block_size}>'

    __repr__ = __str__

    def encrypt(self, message):
        """
        The AESEncryptor's instance encrypts `message`.

        Parameters
        ----------
        message: str
            This is a message.

        Returns
        -------
        encrypted: bytes
            The encrypted message.
        iv: bytes
            The initialization vector.
        """

        raw = self.pad(message.encode())
        iv = random_token().encode()

        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return (
            cipher.encrypt(raw),
            iv
        )

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
        message: str
            This is a message.
        """
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(encrypted)).decode()

    def pad(self, raw):
        """
        padding bytes string, using PKCS7.

        Parameters
        ----------
        raw: bytes
            The encoded message.

        Returns
        -------
        padded: bytes
            The padded message.
        """
        padding_size = 16 - len(raw) % 16
        return raw + padding_size * chr(padding_size).encode()

    def unpad(self, padded):
        """
        unpadding bytes string, using PKCS7.

        Parameters
        ----------
        padded: bytes
            The padded message.

        Returns
        -------
        unpadded: bytes
            The encoded message.
        """
        return padded.replace(bytes([padded[-1]]), b'')
