from .auth import AESCryptor
from server.setting import SECRET_KEY

import base64
import secrets


cryptor = AESCryptor(SECRET_KEY)


def decrypt_payload(denc, div):
    # encode by utf-8
    b64enc = denc.encode()
    b64iv = div.encode()

    # decode by base64
    enc = base64.b64decode(b64enc)
    iv = base64.b64decode(b64iv)

    return cryptor.decrypt(enc, iv)