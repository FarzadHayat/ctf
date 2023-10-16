with open("message.txt", "r") as file:
    content = file.read()

nums = map(int, content.split())
nums = list(map(lambda x: x % 37, nums))

text = ""
for num in nums:
    if num in range(26):
        text += chr(num + ord("A"))
    elif num in range(26, 36):
        text += str(num - 26)
    elif num == 36:
        text += "_"

print("picoCTF{" + text + "}")
