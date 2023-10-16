import hashlib

name = b"MORTON"

flag = "picoCTF{1n_7h3_|<3y_of_"

for n in [4, 5, 3, 6, 2, 7, 1, 8]:
    flag += hashlib.sha256(name).hexdigest()[n]

flag += "}"

print(flag)
