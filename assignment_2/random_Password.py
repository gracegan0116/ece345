import random
import string

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

if __name__ == "__main__":
    
    i = 0
    while i < 300:
        i = i + 1
        print (randomStringDigits(8))
        print (randomStringDigits(7))
        print (randomStringDigits(10))
        print (randomStringDigits(6))
        print (randomStringDigits(12))
        print (randomStringDigits(11))
