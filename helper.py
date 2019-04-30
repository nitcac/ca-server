import random
import string


def random_token(n=16):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))
