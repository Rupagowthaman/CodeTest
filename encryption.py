
#Aufgabe 3:
# # Funktionsdefinition
# def verschiebung(zeichen, schluessel):
#     zahl = ord(zeichen)
#     neueZahl = zahl + schluessel
#     neuesZeichen = chr(neueZahl)
#     return neuesZeichen
# # Funktionsaufrufe
# if __name__=="__main__":

#     print(verschiebung('P', 7))
#     print(verschiebung('A', 3))
#     print(verschiebung('T', 10))



#Aufgabe 5:
def verschiebung(zeichen, schluessel):
    zahl = ord(zeichen)
    neueZahl = zahl + schluessel
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

def encrypt(text,key):
    a=len(text)
    c=" "
    for i in text:
        b = ord(i)
        newnum= b + key 
        if newnum == 91:
            newnum = 65
        newval = chr(newnum)
        c= c + newval
    return c
    print(f"The encrepted value is: " , +c)

def decrypt(text,key):
    a=len(text)
    c=" "
    for i in text:
        b = ord(i)
        newnum= b - key 
        if newnum == 62:
            newnum = 88
        newval = chr(newnum)
        c= c + newval
    return c
    print(f"The encrepted value is: " , +c)


if __name__=="__main__":
    print(f'The encrypt letter for g is :', verschiebung('g',4))
    print(f'The encrypted String :',encrypt('ASTERIX', 3))
    print(f'The Decrypted String :', decrypt('DVWHULA',3))


#Aufgabe 4:
# def encrypt(text,key):
#     a=len(text)
#     c=" "
#     for i in text:
#         b = ord(i)
#         newnum= b + key 
#         if newnum == 91:
#             newnum = 65 
#         newval = chr(newnum)
#         c= c + newval
#     return c
#     print(f"The encrepted value is: " , +c)

# # Funktionsaufrufe
# if __name__=="__main__":
#     print(f"The encrepted value is: ",encrypt('ASTERIX', 3))

