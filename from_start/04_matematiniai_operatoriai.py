## 1
# Sukurkite kintamuosius x, y ir z ir priskirkite jiems atitinkamai sveikąjį skaičių, slankiojo kablelio skaičių ir kompleksinį skaičių.
x = int(input("iveskite skaiciu x: "))
y = float(input("iveskite skaiciu su kableliu y: "))
z = complex(input("Iveskite kompleksini skaiciu z: "))

# sudėties operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame atsakymas1.
atsakymas1 = x + y

# atimties operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame atsakymas2.
atsakymas2 = x - y

# daugybos operaciją su kintamaisiais x, y ir y ir išsaugokite rezultatą kintamajame atsakymas3.
atsakymas3 = x * y

# dalybos operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame atsakymas4.
atsakymas4 = x / y

# keliamosios laipsnio operaciją su kintamaisiais x ir y ir išsaugokite rezultatą kintamajame atsakymas5.
atsakymas5 = x ** y

# Atspausdinkite visus penkis rezultatus.
print(atsakymas1, atsakymas2, atsakymas3, atsakymas4, atsakymas5)

## 2
# Iššūkis 💡: Perdarykite pirmąją užduotį, tik vietoj kintamojo y panaudokite z kintamąjį.
ats1 = x + z
ats2 = x - z
ats3 = x * z
ats4 = x / z
ats5 = x ** z

print(ats1, ats2, ats3, ats4, ats5)

## 3
# Sukurkite kintamąjį a ir priskirkite jam bet kokį sveikąjį skaičių. (int)
a = int(input("Iveskite norima skaiciu kuris vadinsis a: "))

# Sukurkite kintamąjį b ir priskirkite jam bet kokį slankiojo kablelio skaičių. (float)
b = float(input("Iveskite norima skaiciu su kableliu kuris vadinsis b: "))

# Atlikite šalutinę dalybos operaciją su kintamaisiais a ir b ir išsaugokite rezultatą kintamajame atsakymas1.
atsakymas1 = a // b

# Atlikite liekanos operaciją su kintamaisiais a ir b ir išsaugokite rezultatą kintamajame atsakymas2. Atspausdinkite abu rezultatus.
atsakymas2 = a % b

print(atsakymas1, atsakymas2)