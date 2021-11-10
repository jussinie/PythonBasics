# Listat
# Toimivat samoin kuin Javassa, hieman eri syntaksi

lista = [1,2,3,6,5,4]
print(lista)
lista[1] = 4
print(lista)

print(f"Listan pituus on {len(lista)}")


# Listaa voidaan manipuloida lisäämällä alkioita

print("Lisää loppuun komennolla append, tiettyyn indeksiin komennolla insert")
lista.append(5)
print(lista)
lista.insert(0,10)
print(lista)

# Tietystä indeksistä poistetaan komennolla pop (lisäksi palauttaa), tietty luku komennolla remove.

luku = lista.pop(0)
print(lista)
print(f"Poistettu luku on {luku}")

# Onko arvoa listalla? 
etsittava = int(input("Anna etsittävä luku: "))
if etsittava in lista:
	print(f"Luku {etsittava} on listalla.")
else:
	print(f"Lukua {etsittava} ei ole listalla.")

# Sorttaus tapahtuu metodilla sort tai funktiolla sorted (joka luo uuden listan)

jarj_lista = sorted(lista)
print(f"Järjestetty uusi lista: {jarj_lista}")

# Suurin, pienin ja summa saadaan funktioilla max, min ja sum. Funktio ottaa listan parametrikseen. 

print(sum(lista))