flag = open("enc", "r").read()

decoded = flag.encode("utf-16-be")

print(decoded)
