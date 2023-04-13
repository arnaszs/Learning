import random
def spejimas():
    slaptas_skaicius = random.randint(1, 100)
    num_spejimas = 0
    
    while True:
        spejamas_skaicius = int(input("Atspėk numerį nuo 1 - 100: "))
        num_spejimas += 1
        
        if spejamas_skaicius == slaptas_skaicius:
            print("\U00002B50 \U00002705 Sveikinu! Tu atspėjai numerį iš", num_spejimas, "bandymų! \U00002705 \U00002B50")
            break
        elif spejamas_skaicius < slaptas_skaicius:
            print("\U0000274C Skaičius yra per žemas, spėk dar kartą! \U0000274C")
        else:
            print("\U0000274C Skaičius yra per aukštas, spėk dar kartą! \U0000274C")
spejimas()