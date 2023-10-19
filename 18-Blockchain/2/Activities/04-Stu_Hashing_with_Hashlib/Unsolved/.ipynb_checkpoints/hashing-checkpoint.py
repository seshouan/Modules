import hashlib

# output sha256 hash in hexadecimal string format
def hash(message):
    return hashlib.sha256(message).hexdigest()

# modify these messages
# note: we include the "b" before the string definition in order to represent it as bytes instead of a string
message_one = b"hello world"

message_two = b"Hello World"

# print both messages and their corresponding hashes
print(f'msg1: {message_one}')
print(f'msg2: {message_two}')

# compare the hashes in an if/else statement

hash_one = hash(message_one)

hash_two = hash(message_two)

if (hash_one == hash_two):
    print('The messages are the same')
else:
    print('Different messages')

# compare the length of the hashes

print(len(hash_one))
print(len(hash_two))
