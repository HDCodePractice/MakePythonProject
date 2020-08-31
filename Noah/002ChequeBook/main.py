def thingy(n : int) -> str :
    bruh = ""
    b1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]
    b1dash = ["", " - One", " - Two", " - Three", " - Four", " - Five", " - Six", " - Seven", " - Eight", " - Nine"]
    b2 = ["", "", "Twen", "Thir", "Four", "Fif", "Six", "Seven", "Eigh", "Nine"]
    b3 = ["Hundred", "Thousand", "teen", "ty"]
    if n == 0 :
        bruh += "Zero"
    if n <= 12 :
        bruh += "%s"%(b1[n])
    elif n >= 13 and n <= 19 :
        bruh += "%s%s"%(b2[n%10],b3[3])
    else :
    
        bruh += "%s%s%s"%(b2[int(n/10)],b3[3],b1dash[n%10])
    if n != 1 :
        bruh += " Dollars"
    else :
        bruh += " Dollar"
    return bruh
for i in range(0,99):
    print("%s"%(thingy(i)))
