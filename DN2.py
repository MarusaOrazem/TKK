abeceda = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}




#LFSR1 ima v našem primeru karakteristični polinom enak p(x) = x^5 + x^2 + 1
#LFSR2 pripada p(x) = x^7 + x^1 + 1
#LFSR3 pripada p(x) = x^11 + x^2 + 1
#iz tega vemo rekurzivno zvezo in znamo naprej setsaljati ključ in zakriptirati besedilo


def LFSR1(besedilo, zac_kluc):
    #sestavimo cel kjuč, dolžine enake kot besedilo
    kluc = zac_kluc
    for indeks in range(5,len(besedilo)):
        kluc += str((int(kluc[indeks-2]) + int(kluc[indeks-5]))%2)
    kriptirano = ''
    for znak in besedilo:
        vrednost = abeceda[znak]
        bin_vrednost = str(bin(vrednost)[2:])
        dolzina = len(bin_vrednost)
        while dolzina != 5:
            bin_vrednost = '0' + bin_vrednost
            dolzina += 1
        kriptirano += bin_vrednost
    return kriptirano

def LFSR2(besedilo, zac_kluc):
    #sestavimo cel kjuč, dolžine enake kot besedilo
    kluc = zac_kluc
    for indeks in range(5,len(besedilo)):
        kluc += str((int(kluc[indeks-1]) + int(kluc[indeks-7]))%2)
    kriptirano = ''
    for znak in besedilo:
        vrednost = abeceda[znak]
        bin_vrednost = str(bin(vrednost)[2:])
        dolzina = len(bin_vrednost)
        while dolzina != 5:
            bin_vrednost = '0' + bin_vrednost
            dolzina += 1
        kriptirano += bin_vrednost
    return kriptirano

def LFSR3(besedilo, zac_kluc):
    #sestavimo cel kjuč, dolžine enake kot besedilo
    kluc = zac_kluc
    for indeks in range(5,len(besedilo)):
        kluc += str((int(kluc[indeks-2]) + int(kluc[indeks-11]))%2)
    kriptirano = ''
    for znak in besedilo:
        vrednost = abeceda[znak]
        bin_vrednost = str(bin(vrednost)[2:])
        dolzina = len(bin_vrednost)
        while dolzina != 5:
            bin_vrednost = '0' + bin_vrednost
            dolzina += 1
        kriptirano += bin_vrednost
    return kriptirano






#besedilo = 'MARUSAORAZEMJESUPER'
#zac_kluc = '10001'

#print(LFSR1(besedilo,zac_kluc))
