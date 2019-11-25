import random
import string
from pyfiglet import Figlet

# Shows
def init():
    f = Figlet(font='doh')
    print f.renderText('PassX') 

def generatePassword(stringLength=10):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

init()