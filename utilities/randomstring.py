import random
import string

def random_string_generator(size=6,char=string.ascii_lowercase+string.ascii_uppercase+string.digits):
    return ''.join(random.choice(char) for x in range(size))
