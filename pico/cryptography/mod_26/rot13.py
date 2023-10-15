phrase = list("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}")

for i in range(len(phrase)):
    c = phrase[i]
    o = ord(c)
    if c.isalpha():
        if c.isupper():
            offset = ord("A")
        else:
            offset = ord("a")
        phrase[i] = chr((o - offset + 13) % 26 + offset)

print("".join(phrase))
