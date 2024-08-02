
def clamp(x,limit):
    return divmod(x,limit)[1]
def encode(str1,str2):
    out = ""
    for i in range(len(str1)):
        modif = (ord(str1[i])+55000) + (ord(str2[clamp(len(str1)-i, len(str2))]))
        modstr = chr(modif)
        #print(modif, modstr)
        out += modstr
    return out
def decode(msg, key):
    out = ''
    for i in range(len(msg)):
        modif = (ord(msg[i])-55000) - (ord(key[clamp(len(msg)-i, len(key))]))
        #print(modif)
        modstr = chr(clamp(modif,110000))
        #print(modif, modstr)
        out += modstr
    return out



