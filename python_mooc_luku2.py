# Testaillaan if-lauseita
# Muista, että Pythonissa tärkeää on sisennys! Useammat ehtolauseet sisennetään.
ika = int(input("Anna ikäsi: "))
if ika < 18:
    print("Sinullapa ei ole tänne asiaa!")
elif ika > 100:
    print("Eiköhän ole aika mennä jo kotiin?!")
else:
    print(f"Olet {ika} vuotta vanha. Tervetuloa ravintolaan!")

# Loogiset operaattorit toimivat muuten samoin kuin Javassa, mutta ne merkitään and ja or

if ika < 18 and ika > 12:
    print(f"Olet iältäsi {ika}-vuotias, siis teini!")

# While-looppi kirjoitetaan Pyhtonissa seuraavasti: 

counter = 0
while True:
    sana = input("Haluatko lopettaa? ")
    print(sana)
    counter += 1
    if sana == "kyllä":
        break

print(f"Poistuttiin {counter} kierroksen jälkeen.")