from string import ascii_uppercase, digits

with open("message.txt", "r") as file:
    content = file.read()

nums = list(map(int, content.split()))

flag = []
for num in nums:
    modulus = num % 41
    inverse = pow(num, -1, 41)

    if inverse in range(1, 27):
        flag.append(ascii_uppercase[inverse - 1])
    elif inverse in range(27, 37):
        flag.append(digits[inverse - 27])
    elif inverse == 37:
        flag.append("_")

print("picoCTF{%s}" % "".join(flag))
