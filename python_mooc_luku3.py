# Merkkijonojen käsittelyä

def merkkijonot():
    sana1 = input("Anna ensimmäinen merkkijono: ")
    sana2 = input("Anna toinen, enemmän möyhennettävä merkkijono: ")

    print("Pythonissa voi yhdistää +-merkillä:")
    print(sana1 + sana2)

    print("Pythonissa voi monistaa *-merkillä:")
    maara = int(input("Montako kertaa? "))
    print(sana1 * maara)

    print("Merkkijonon 2 pituus saadaan len")
    print(len(sana2))

    # indeksi toimii sekä alusta (0 ->) tai lopusta (-1 ->) alkaen
    print(f"Sanan {sana2} viimeinen kirjain on {sana2[-1]}")

    # Osajonot

    haettava = input("Mitä osajonoa etsitään? ")
    print(haettava in sana2)

if __name__ == "__main__":
    merkkijonot()