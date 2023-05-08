import random

while True:
    kauliukas1 = random.randint(1, 6)
    kauliukas2 = random.randint(1, 6)
    kauliukas3 = random.randint(1, 6)

    print("Skaičiai:", kauliukas1, kauliukas2, kauliukas3)

    if 5 in (kauliukas1, kauliukas2, kauliukas3):
        print("Pralaimėjai...")
        break
    else:
        print("Laimėjai!")
        print("Žaidžiam dar? (t/n)")
        play_again = input()
        if play_again.lower() != "t":
            break

import calendar

def kalendorius(metai, menesis):
    print(calendar.month(metai, menesis))

    _, menesio_ilgis = calendar.monthrange(metai, menesis)

    savaitgaliu_skaicius = 0
    for diena in range(1, menesio_ilgis + 1):
        savaites_diena = calendar.weekday(metai, menesis, diena)
        if savaites_diena == 5 or savaites_diena == 6:
            savaitgaliu_skaicius += 1

    print(f'Savaitgalio dienu skaicius siame menesyje: {savaitgaliu_skaicius}')
    return

kalendorius(2023, 5)

