# generate a password with length "passlen" with no duplicate characters in the password

import random
length = input("enter password length: ")
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = length
p =  "".join(random.sample(s,passlen ))
print p
