## 1
# Parašykite programą, kuri leidžia vartotojui įvesti bet kokią simbolių eilutę ir atspausdina jos pirmąjį ir paskutinį simbolius.
a = str(input("iveskite norima teksta: "))
print(a[0], a[-1])

## 2
# Sukurkite simbolių eilutę, kurią sudaro jūsų mėgstamos knygos pavadinimas. Atspausdinkite jo pirmąsias penkias raides.
a = str(input("iveskite savo megstamos knygos pavadinima: "))
print(a[:5])

## 3
# Sukurkite simbolių eilutę, kurią sudaro jūsų mėgstama citata. Atspausdinkite jo paskutines tris raides.
a = str(input("Iveskite savo megstama citata: "))
print(a[-3:])

## 4
# Sukurkite programą, kuri leidžia vartotojui įvesti du skirtingus žodžius ir atspausdina kiekvieno žodžio pirmuosius simbolius,
# atskirtus brūkšneliu. Pvz., "Labas vakaras" ir "geros dienos" -> "L-v", "g-d". Naudokite du kintamuosius įvedimui.
pirmas = str(input("Iveskite pirmaji zodi: "))
antras = str(input("iveskite antraji zodi: "))
print(pirmas[0] + "-" + antras[0])

## 5
# Sukurkite tekstą "Aš esu studentas".
a = "As esu studentas"
# Panaudokite upper metodą, kad pakeistumėte visas raides didžiosiomis.
print(a.upper())
# Panaudokite lower metodą, kad pakeistumėte visas raides mažosiomis.
print(a.lower())
# Panaudokite join metodą, kad sujungtumėte žodžių sąrašą ["Aš", "esu", "studentas"] į vieną eilutę su tarpais tarp žodžių.
sarasas = ["As", "esu", "studentas"]
eilutes = " ".join(sarasas)
print(eilutes)
# Panaudokite split metodą, kad padalintumėte eilutę "Aš esu studentas" į žodžių sąrašą.
sarasas = a.split(" ")
print(sarasas)
# Panaudokite find metodą, kad rastumėte poziciją, kurioje prasideda žodis "studentas" eilutėje "Aš esu studentas".
sarasas = a.find("studentas")
print(sarasas)
# Panaudokite replace metodą, kad pakeistumėte žodį "studentas" žodžiu "programuotojas" eilutėje "Aš esu studentas".
sarasas = a.replace("studentas", "programuotojas")
print(sarasas)

## 6
# Paprašykite vartotojo įvesti savo vardą ir amžių. Tada išveskite pranešimą, kuriame nurodomi vartotojo vardas ir metai, kai vartotojui sukaks 100 metų.
vardas = str(input("Iveskite savo varda: "))
metai = int(input("Iveskite savo amziu"))
iki_100 = 100 - int(metai)
will_be = 2024 + iki_100
print(f"Sveiki {vardas} jums bus 100 metu, {will_be} metais")

## 7
# Parašykite programą, kuri paprašytų vartotojo įvesti savo ūgį centimetrais.
# Tada programą turi paversti vartotojo ūgį metrais ir išvesti pranešimą su vartotojo ūgiu abiejomis matavimo vienetų.
ugis = int(input("iveskite savo ugi centimetrais: "))
metrais = ugis / 100
print(f"Jusu ugis centimetrais: {ugis}, metrais - {metrais}")

## 8
# Paprašykite vartotojo įvesti savo atlyginimą ir taikomą mokesčio procentą.
# Tada apskaičiuokite, kiek vartotojas gaus mėnesio pabaigoje, kai nuo atlyginimo bus nuskaičiuotas mokesčio procentas.
atlygis = input("iveskite savo atlyginima pries mokescius: ")
procentas = input("iveskite koki procenta pasiema mokesciai: ")
mokesciai = (int(atlygis) / 100) * int(procentas)
atlyginimas = int(atlygis) - int(mokesciai)
print(atlyginimas)

## 9
# Sukurkite programą, kuri leistų vartotojui pasirinkti, kokią konversiją jis nori atlikti:
# arba keisti temperatūrą iš laipsnių Celsijaus į laipsnius Farenheito, arba iš laipsnių Farenheito į laipsnius Celsijaus.
# Tada programa turi paprašyti vartotojo įvesti pradinę temperatūrą ir atlikti konversiją bei išvesti rezultatą.
print("Sveiki, pasirinkite norima uzduoti: ")
print("1 - paversti celsiu i farenheita")
print("2 - paversti farenheita i celsiju")
pasirinkimas = input("Iveskite savo pasirinkima: ")
temp = (input("iveskite temperatura: "))

if pasirinkimas == "1":
    farenheit = float(temp) * 9/5 + 32
    print(f"{temp} laipsniu celsijaus yra {farenheit} laipsniu farenheito.")
elif pasirinkimas == "2":
    celsius = float(temp) * 5/9 - 32
    print(f"{temp} laipsniu farenheito yra {celsius} laipsniu celsijaus")
else:
    print("Netinkamas skaicius")