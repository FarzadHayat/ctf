# the given hex number
hex_num = "0x70"

# convert to base 10
num = int(hex_num, 16)

# get ASCII char of num
char = chr(num)

# print flag
print("picoCTF{%s}" % char)
