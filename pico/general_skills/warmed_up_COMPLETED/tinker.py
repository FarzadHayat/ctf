# given base 16 number
hex_num = "0x3D"

# convert to base 10
num = int(hex_num, 16)

# print flag
print("picoCTF{%s}" % num)
