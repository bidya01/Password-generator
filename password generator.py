import random
import string

def password_gen(size,chars= string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits):
    return ''.join(random.choice(chars) for i in range(1,size))

print(password_gen(int(input('How many characters in your password?'))))
