## 1
# Parašykite programą, kuri nustatytų, ar vartotojo įvestas skaičius yra teigiamas, naudodami daugiau operatorių.
# Jei skaičius yra teigiamas, turi būti spausdinamas pranešimas "Skaičius yra teigiamas", o jei ne - "Skaičius yra neigiamas".

a = int(input("Iveskite norima skaiciu: "))
if a > 0:
    print(f"Skaicius {a} yra teigiamas")
else:
    print(f"Skaicius {a} yra neigiamas")

## 2
# Parašykite programą, kuri patikrintų, ar vartotojo įvestas skaičius yra tarp 5 ir 10, naudodama mažiau arba lygu operatorių.
# Jei skaičius yra tarp 5 ir 10, turi būti spausdinamas pranešimas "Skaičius yra tarp 5 ir 10", o jei ne - "Skaičius nėra tarp 5 ir 10".
a = int(input("Iveskite norima skaiciu: "))
if a >= 5 and a <= 10:
    print(f"Skaicius {a} yra tarp 5 ir 10")
else:
    print(f"Skaicius {a} nera tarp 5 ir 10")

## 3
# Parašykite programą, kuri patikrintų, ar du skaičiai yra didesni nei 0, naudodami "ir" operatorių.
# Jei abu skaičiai yra didesni nei 0, turi būti spausdinamas pranešimas "Abu skaičiai yra didesni nei 0", o jei ne - "Bent vienas skaičius yra neigiamas arba lygus 0".
a = int(input("Iveskite pirmaji norima skaiciu: "))
b = int(input("Iveskite antraji norima skaiciu: "))
if a and b > 0:
    print(f"Abu skaiciai - {a} ir {b} yra didesni nei 0")
else:
    print(f"Bent vienas skaicius {a} arba {b} yra neigiamas arba lygus 0")

## 4
# Parašykite programą, kuri nustatytų, ar bent vienas duotų skaičių yra lyginis, naudodami "arba" operatorių.
# Jei bent vienas skaičius yra lyginis, turi būti spausdinamas pranešimas "Bent vienas skaičius yra lyginis", o jei ne - "Abu skaičiai yra nelyginiai".
a = int(input("Iveskite pirmaji norima skaiciu: "))
b = int(input("Iveskite antra norima skaiciu: "))
if a % 2 == 0 or b % 2 == 0:
    print(f"Bent vienas skaicius - {a} arba {b} yra lyginis")
else:
    print(f"Abu skaiciai {a} ir {b} yra nelyginiai")