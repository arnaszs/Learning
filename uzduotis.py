atlygis = input("Iveskite savo atlygi: ")
procentas = input("Iveskite savo mokesciu procenta: ")
neto = int(atlygis) * (1 - int(procentas) / 100)
print(f"Jusu atlyginimas i rankas yra {neto:.x2f} EUR")