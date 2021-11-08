# Python - Ohjelmoinnin perusteet, osa 1

print("Hello World! :->")
print("Starting using Python")

# harjoitellaan muuttujia

nimi = input("Anna nimesi: ")
print("Moi, " + nimi)

# Pythonissa muuttujissa sanojen välissä alaviiva, Javassa ja JavaScriptissa CamelBack.
# Eli käytännössä:

pitka_muuttuja = "lentokonemekaanikko"
print("Yksi pitkä muuttuja on " + pitka_muuttuja)

# Tulostaminen: voidaan tehdä plussalla, mutta tällöin ei voi tulostaa eri tyyppejä (esim str ja int).
# Se onnistuu kuitenkin käyttämällä pilkkua tai muuttamalla muuttujan tyyppi. 
print("Lukuarvo on ", 24)
print("Sama lukuarvo on " + str(24))

# Pythonissa näyttää olevan myös niin sanottu f-merkkijono, joka muistuttaa JavaScriptin template stringiä `testiarvo on ${arvo}`
print(f"testiarvo on {24}")

# Liukuluvut (floats) toimivat desimaalilukujen tavoin. Javassa on myös float f = 1.01f, joka on eri asia kuin double. 
# Double is a 64-bit precision IEEE 754 floating point, while float is a 32-bit precision IEEE 754 floating point.
# Kokeillaan keskiarvon laskemista: 

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))

keskiarvo = (luku1 + luku2 + luku3) / 3
print(f"Lukujen keskiarvo on {keskiarvo}")