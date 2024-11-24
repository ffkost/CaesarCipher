
bukva = input("Vnesete s za sifrirane ili d za desifrirane ")
text = input("Vnesi text:   ")
shift = int(input("Vnesi Shift parametar"))

def shifriraj(t, s):
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    sifriran_text = ""
    for i in t:
        if i.isalpha():
            pozicija = lista.index(i)
            # Use modulus to wrap the index correctly
            sifra = lista[(pozicija + s) % len(lista)]
            sifriran_text = sifriran_text + sifra
        else:
            sifriran_text = sifriran_text + i

    return sifriran_text

def deshifriraj(t, s):
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    sifriran_text = ""
    for i in t:
        if i.isalpha():
            pozicija = lista.index(i)
            # Use modulus to wrap the index correctly
            sifra = lista[(pozicija - s) % len(lista)]
            sifriran_text = sifriran_text + sifra
        else:
            sifriran_text = sifriran_text + i

    return sifriran_text

def funkcija(text,bukva,shift):
    if bukva == "s":
        print(shifriraj(text, shift))
    elif bukva == "d":
        print(deshifriraj(text, shift))



funkcija(text, bukva, shift)

