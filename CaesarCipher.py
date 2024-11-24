import random
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
signs = ['(', ')', '*', '&', '#', '@', '%', '$', '!', '?']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_pw = []
mali_bukvi = int(input("Vnesi kolku mali bukvi sakas da ima vo passwordot "))
golemi_bukvi = int(input("Vnesi kolku golemi bukvi sakas da ima vo passwordot "))
znaci = int(input("Vnesi kolku znaci sakas da ima vo passwordot: "))
shift = random.randint(1, 10)
for i in range(mali_bukvi):
    pozicija = random.randint(0, len(lowercase_letters) - 1)
    sifra = lowercase_letters[(pozicija + shift) % len(lowercase_letters)]
    lista_pw.append(sifra)
for i in range(golemi_bukvi):
    pozicija = random.randint(0, len(uppercase_letters) - 1)
    sifra = uppercase_letters[(pozicija + shift) % len(uppercase_letters)]
    lista_pw.append(sifra)
for i in range(znaci):
    pozicija = random.randint(0, len(signs) - 1)
    sifra = signs[(pozicija + shift) % len(signs)]
    lista_pw.append(sifra)
random.shuffle(lista_pw)
password_text = ""
for i in lista_pw:
    password_text = password_text + i  # vtor nacin 2
print(password_text)
#password_text = "".join(lista_pw) # lista da ja napravime vo text  # tret nacin
#print(password_text)


#print(lista_pw) #1

#print(lista_pw) #
