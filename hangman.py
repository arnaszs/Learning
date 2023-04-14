import random

# galimi žodžiai
words = ['smėlis', 'agurkas', 'italija', 'deimantas', 'sekme',\
          'kursai', 'paskaitos', 'pomidoras', 'krepšinis']

# Pasirinkti random žodį
zodis = random.choice(words)

# listas storint spėjimus
spejimai = []

# Ėjimų skaičius
ejimai = 10

# Begalinis ratas, iki kol žaidėjas atspėja žodį arba baigiasi spėjimai
while ejimai > 0:
    rodyti = ''
    for raides in zodis:
        if raides in spejimai:
            rodyti += raides
        else:
            rodyti += '_ '
    print(rodyti)

    # Paklausti žaidėjo spėti raidę
    spejimas = input('Spėk raidę: ')

    # Patikriname ar raidė yra žodyje
    if spejimas in zodis:
        spejimai.append(spejimas)
        print('Teisingai!')
    else:
        ejimai -= 1
        print('Neteisingai! Tau liko', ejimai, 'spėjimai')

    # Patikrinti ar žaidėjas spėjo žodį
    if all(raide in spejimai for raide in zodis):
        print('Sveikinimai! Jūs atspėjote žodį:', zodis)
        break

# Jaigu žaidėjui baigiasi spėjimai, atskleidžiame žodį
if ejimai == 0:
    print('Atsiprašau, tu pritrūkai ėjimų. Žodis buvo:', zodis)