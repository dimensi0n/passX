import random
import string
from pyfiglet import Figlet

# Shows
def init():
    f = Figlet(font='doh')
    print(f.renderText('PassX')) 

def generatePassword(stringLength=10):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def main():
    length = int(input("How many characters do you want ?"))
    print(generatePassword(length))

if __name__ == "__main__":
    init()
    main()    