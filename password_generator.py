import secrets
import string

name = "Yelyzaveta"
length = len(name)

hex_digits = "0123456789abcdef"
punctuation = string.punctuation
uppercase = string.ascii_uppercase

password_chars = [
    secrets.choice(hex_digits),
    secrets.choice(punctuation),
    secrets.choice(uppercase),
]

all_chars = hex_digits + punctuation + uppercase

for _ in range(length - len(password_chars)):
    password_chars.append(secrets.choice(all_chars))

secrets.SystemRandom().shuffle(password_chars)
password = "".join(password_chars)

print("Ім'я:", name)
print("Довжина пароля:", length)
print("Згенерований пароль:", password)
print("Пароль у шістнадцятковому форматі:", password.encode("utf-8").hex())