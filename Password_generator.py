import random
import string
def password_generator(length=12):
  letters = string.asiic_letters
  number = string.digits
  symbols = string.puncutations
  all_char = letters + number + symbols
  password = "".join([random.choice(all_char) for _ in range(length)])
  
  return password_generator()
print(password_generator(12))                     
  
