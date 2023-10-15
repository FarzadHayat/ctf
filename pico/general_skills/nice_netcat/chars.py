file = open("input.txt", "r")
lines = file.read().splitlines()

flag = ""
for line in lines:
    flag += chr(int(line.strip()))

print(flag)
