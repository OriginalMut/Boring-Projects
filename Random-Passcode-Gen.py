    # random models
import random
import string
    #define charchters
characters = string.ascii_letters + string.digits + string.punctuation
    #define password length
password_length = 16    
    #generate random password
password = "".join(random.choice(characters) for i in range(password_length))
    #ensure at least one kind of each character
password = ( random.choice(string.ascii_lowercase) 
            + random.choice(string.ascii_uppercase) 
            + random.choice(string.digits) 
            + random.choice(string.punctuation) 
    #Fill rest of password with ength with random choices
            + "".join(random.choice(characters) for i in range(password_length - 4)) )
    #shuffle password
password + ''.join(random.sample(password, len(password)))
    #print password
print("Generated password: ", password)
