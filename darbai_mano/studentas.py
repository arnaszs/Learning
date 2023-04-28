class Studentas:
    def __init__(self, vardas, pavarde, amzius):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius

    @property
    def pilnas_vardas(self):
     return f"{self.vardas} {self.pavarde}"

    @staticmethod
    def ar_pilnametis(amzius):
        return amzius >= 18

    @classmethod
    def sukurti_studenta(cls, vardas: str, pavarde: str, amzius: int):
        return cls(vardas, pavarde, amzius)

studentas1 = Studentas.sukurti_studenta("Jonas", "Jonaitis", 19)
studentas2 = Studentas.sukurti_studenta("Petras", "Petraitis", 5)

print(Studentas.ar_pilnametis(studentas1.amzius))
print(Studentas.ar_pilnametis(studentas2.amzius))