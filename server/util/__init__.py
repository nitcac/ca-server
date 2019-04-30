from .decrypt import AESDecryptor
from server.setting import SECRET_KEY

import base64
import secrets


sec = "XiZEFzMPsvbIaanO"
cryptor = AESDecryptor(sec)


def decrypt_payload(enc, iv):
    # encode by utf-8
    b64enc = enc.encode()
    b64iv = iv.encode()

    # decode by base64
    enc = base64.b64decode(b64enc)
    iv = base64.b64decode(b64iv)

    return cryptor.decrypt(enc, iv)