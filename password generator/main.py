import random
import string

def generate(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(all_chars) for i in range(length))
    
    return password
password = generate(10)
print(password)
