import random
def spejimas():
    slaptas_skaicius = random.randint(1, 100)
    num_spejimas = 0
    
    while True:
        spejamas_skaicius = int(input("atspėk numerį nuo 1 - 100: "))
        num_spejimas += 1
        
        if spejamas_skaicius == slaptas_skaicius:
            print("Sveikinu! Tu atspėjai numerį iš", num_spejimas, "bandymų!")
            break
        elif spejamas_skaicius < slaptas_skaicius:
            print("Skaičius yra per žemas, spėk dar kartą!")
        else:
            print("Skaičius yra per aukštas, spėk dar kartą!")
spejimas()