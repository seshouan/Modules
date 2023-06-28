# import required libraries
import random
import string

# function to generate UUID - default length is 4 characters
def uuid_generator(length=4, codebase="abc"):
    result = random.choices(codebase, k=length)
    return "".join(result)

# print generated UUID
print(f"New UUID: {uuid_generator(7,string.ascii_letters+string.digits)}")
