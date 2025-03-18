import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from app.config.settings import settings


def decrypt_credentials(credentials: str) -> str:
    IV = settings.AUTH_TOKEN_IV.encode('utf-8')
    KEY = base64.b64decode(settings.AUTH_TOKEN_KEY)

    cipher = AES.new(KEY, AES.MODE_CBC, IV)

    credentials = base64.b64decode(credentials)

    return unpad(cipher.decrypt(credentials), 16).decode('utf-8')


def encrypt_credentials(credentials: str) -> str:
    IV = settings.AUTH_TOKEN_IV.encode('utf-8')
    KEY = base64.b64decode(settings.AUTH_TOKEN_KEY)

    cipher = AES.new(KEY, AES.MODE_CBC, IV)

    credentials = cipher.encrypt(pad(credentials.encode('utf-8'), 16))

    return base64.b64encode(credentials).decode('utf-8')
